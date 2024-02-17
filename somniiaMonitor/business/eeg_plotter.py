#  Copyright (c) Matteo Ferreri 2024.

import queue
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from somniiaMonitor.model.eeg_signal_data import EegSignalData

_MAX_POINTS_ON_X = 10


class EegPlotter:
    def __init__(self):
        self._fig, self._ax = plt.subplots()
        plt.title("Eeg Graph")
        plt.xlabel("time [ms]")
        plt.subplots_adjust(bottom=0.15)
        self._times_data = []
        self._first_channel_data = []
        self._second_channel_data = []
        self._third_channel_data = []
        self._line_first_channel, = self._ax.plot(self._times_data, self._first_channel_data, color="black")
        self._line_second_channel, = self._ax.plot(self._times_data, self._second_channel_data, color="red")
        self._line_third_channel, = self._ax.plot(self._times_data, self._third_channel_data, color="blue")
        self.queue = queue.Queue()

    def get_figure(self):
        return self._fig

    def get_ax(self):
        return self._ax

    @staticmethod
    def get_gcf():
        return plt.gcf()

    def init_plot(self):
        return self._line_first_channel,

    def add_data(self, data: EegSignalData):
        self.queue.put(data)

    def update_plots(self, frame):
        try:
            eeg_data: EegSignalData = self.queue.get()
            self._times_data.append(int(eeg_data.get_time()))
            self._first_channel_data.append(int(eeg_data.get_first_channel()))
            self._second_channel_data.append(int(eeg_data.get_second_channel()))
            self._third_channel_data.append(int(eeg_data.get_third_channel()))
            self._line_first_channel.set_data(self._times_data, self._first_channel_data)
            self._line_second_channel.set_data(self._times_data, self._second_channel_data)
            self._line_third_channel.set_data(self._times_data, self._third_channel_data)
            self._ax.relim()
            self._ax.autoscale_view()
            if len(self._times_data) > _MAX_POINTS_ON_X:
                self._ax.set_xlim(self._times_data[-_MAX_POINTS_ON_X], self._times_data[-1])
        except queue.Empty:
            pass
        # return self._line_first_channel,

    def run(self):
        anim = FuncAnimation(self._fig, self._update_plots, frames=None, interval=200,
                             cache_frame_data=False)

        return anim

    @staticmethod
    def set_title(title: str):
        plt.title(title)

    @staticmethod
    def set_x_axis_name(x_name: str):
        plt.xlabel(x_name)

    @staticmethod
    def set_y_axis_name(y_name: str):
        plt.ylabel(y_name)

    @staticmethod
    def add_grid_lines():
        plt.grid()

    def set_first_channel_visible(self, value: bool):
        self._line_first_channel.set_visible(value)

    def set_second_channel_visible(self, value: bool):
        self._line_second_channel.set_visible(value)

    def set_third_channel_visible(self, value: bool):
        self._line_third_channel.set_visible(value)

