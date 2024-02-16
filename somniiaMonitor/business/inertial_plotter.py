#  Copyright (c) Matteo Ferreri 2024.

import queue
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

from somniiaMonitor.model.inertial_parameter_data import InertialParameterData

_MAX_POINTS_ON_X = 10


class InertialPlotter:
    def __init__(self):
        plt.title = "Inertial Graph"
        plt.xlabel("time")
        self._fig, self._rms = plt.subplots()
        self._roll = self._rms.twinx()
        self._pitch = self._roll.twinx()
        self._yaw = self._pitch.twinx()
        self._times_data = []
        self._rms_data = []
        self._roll_data = []
        self._pitch_data = []
        self._yaw_data = []
        self._line_rms = self._rms.plot(self._times_data, self._rms_data)
        self._line_roll = self._roll.plot(self._times_data, self._roll_data)
        self._line_pitch = self._pitch.plot(self._times_data, self._pitch_data)
        self._line_yaw = self._yaw.plot(self._times_data, self._yaw_data)
        self.queue = queue.Queue()

    def get_figure(self):
        return self._fig

    def get_ax(self):
        return self._rms

    @staticmethod
    def get_gcf():
        return plt.gcf()

    def init_plot(self):
        return self._line_rms,

    def add_data(self, data: InertialParameterData):
        self.queue.put(data)

    def update_plots(self, frame):
        try:
            value: InertialParameterData = self.queue.get()
            self._times_data.append(value.get_time())
            self._rms_data.append(value.get_root_mean_square())
            self._roll_data.append(value.get_roll())
            self._pitch_data.append(value.get_pitch())
            self._yaw_data.append(value.get_yaw())
            self._line_rms.set_data(self._times_data, self._rms_data)
            self._line_roll.set_data(self._times_data, self._roll_data)
            self._line_pitch.set_data(self._times_data, self._pitch_data)
            self._line_yaw.set_data(self._times_data, self._yaw_data)
            self._rms.relim()
            self._roll.relim()
            self._pitch.relim()
            self._yaw.relim()
            self._rms.autoscale_view()
            self._roll.autoscale_view()
            self._pitch.autoscale_view()
            self._yaw.autoscale_view()
            if len(self._times_data) > _MAX_POINTS_ON_X:
                self._rms.set_xlim(self._times_data[-_MAX_POINTS_ON_X], self._times_data[-1])
                self._roll.set_xlim(self._times_data[-_MAX_POINTS_ON_X], self._times_data[-1])
                self._pitch.set_xlim(self._times_data[-_MAX_POINTS_ON_X], self._times_data[-1])
                self._yaw.set_xlim(self._times_data[-_MAX_POINTS_ON_X], self._times_data[-1])
        except queue.Empty:
            pass
        return self._line_rms,

    def run(self):
        anim = FuncAnimation(self._fig, self._update_plots, frames=None, interval=200,
                             cache_frame_data=False)
        return anim

