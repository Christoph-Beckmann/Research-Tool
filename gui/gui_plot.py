import logging
import tkinter as tk
import gui_helpers
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

logger = logging.getLogger(__name__)


class GUIPlot(tk.Toplevel):
    def __init__(self, parent, data, keywords):
        super().__init__(parent)

        self_width = 500
        self_height = 500

        center_x, center_y = gui_helpers.center_form(self, self_width, self_height)
        self.geometry(f"{self_width}x{self_height}+{center_x}+{center_y}")
        self.title("Research Tool - Figure")
        self.configure(bg="#EEEEEE")

        self.plot(data, keywords)

        self.resizable(True, True)

    def plot(self, data, keywords):
        figure = Figure(figsize=(50, 50), dpi=100)
        plt = figure.add_subplot(1, 1, 1)

        for keyword in keywords:
            plt.plot(data.index, data[keyword], label=keyword)
        plt.legend()

        canvas = FigureCanvasTkAgg(figure, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0)
