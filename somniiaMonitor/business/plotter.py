#  Copyright (c) Matteo Ferreri 2024.

import queue
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

_MAX_POINTS_ON_X = 10


class Plotter:
    def __init__(self):
        self._fig, self._ax = plt.subplots()
        self._x_data, self._y_data = [], []
        self._line, = self._ax.plot(self._x_data, self._y_data)
        self.queue = queue.Queue()

    def get_figure(self):
        return self._fig

    def get_ax(self):
        return self._ax

    @staticmethod
    def get_gcf():
        return plt.gcf()

    def init_plot(self):
        return self._line,

    def add_data(self, x, y):
        self.queue.put((x, y))

    def update_plots(self, frame):
        try:
            value = self.queue.get()
            self._x_data.append(value[0])
            self._y_data.append(value[1])
            self._line.set_data(self._x_data, self._y_data)
            print(f"x:{self._x_data[-1]}, y:{self._y_data[-1]}")
            self._ax.relim()
            self._ax.autoscale_view()
            if len(self._x_data) > _MAX_POINTS_ON_X:
                self._ax.set_xlim(self._x_data[-_MAX_POINTS_ON_X], self._x_data[-1])
        except queue.Empty:
            pass
        return self._line,

    def run(self):
        anim = FuncAnimation(self._fig, self._update_plots, frames=None, interval=200,
                             cache_frame_data=False)
        return anim
