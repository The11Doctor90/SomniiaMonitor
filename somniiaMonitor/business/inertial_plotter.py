#  Copyright (c) Matteo Ferreri 2024.
import datetime
import queue
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

from somniiaMonitor.model.inertial_parameter_data import InertialParameterData

_MAX_POINTS_ON_X = 10


class InertialPlotter:
    def __init__(self):
        self._fig, self._ax = plt.subplots()
        plt.title("Inertial Graph")
        plt.xlabel("time [ms]")
        plt.subplots_adjust(bottom=0.15)
        self._times_data = []
        self._rms_data = []
        self._roll_data = []
        self._pitch_data = []
        self._yaw_data = []
        self._line_rms, = self._ax.plot(self._times_data, self._rms_data, color="black", label="RSM")
        self._line_roll, = self._ax.plot(self._times_data, self._roll_data, color="red", label="Roll")
        self._line_pitch, = self._ax.plot(self._times_data, self._pitch_data, color="blue", label="Pitch")
        self._line_yaw, = self._ax.plot(self._times_data, self._yaw_data, color="green", label="Yaw")
        self.queue = queue.Queue()

    def get_figure(self):
        return self._fig

    def get_ax(self):
        return self._ax

    @staticmethod
    def get_gcf():
        return plt.gcf()

    def init_plot(self):
        return self._line_rms,

    def add_data(self, data: InertialParameterData):
        self.queue.put(data)

    def update_plots(self, frame):
        try:
            inertial_data: InertialParameterData = self.queue.get()
            self._times_data.append(int(inertial_data.get_time()))
            self._rms_data.append(float(inertial_data.get_root_mean_square()))
            self._roll_data.append(float(inertial_data.get_roll()))
            self._pitch_data.append(float(inertial_data.get_pitch()))
            self._yaw_data.append(float(inertial_data.get_yaw()))
            self._line_rms.set_data(self._times_data, self._rms_data)
            self._line_roll.set_data(self._times_data, self._roll_data)
            self._line_pitch.set_data(self._times_data, self._pitch_data)
            self._line_yaw.set_data(self._times_data, self._yaw_data)
            self._ax.relim()
            self._ax.autoscale_view()
            if len(self._times_data) > _MAX_POINTS_ON_X:
                self._ax.set_xlim(self._times_data[-_MAX_POINTS_ON_X], self._times_data[-1])
        except queue.Empty:
            pass
        # return self._line_rms,

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

    def set_rms_visible(self, value: bool):
        self._line_rms.set_visible(value)

    def set_roll_visible(self, value: bool):
        self._line_roll.set_visible(value)

    def set_pitch_visible(self, value: bool):
        self._line_pitch.set_visible(value)

    def set_yaw_visible(self, value: bool):
        self._line_yaw.set_visible(value)
