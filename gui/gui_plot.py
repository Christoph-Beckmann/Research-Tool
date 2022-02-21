import logging
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

logger = logging.getLogger(__name__)


class GUIPlot(tk.Toplevel):
    def __init__(self, parent, data, keywords):
        super().__init__(parent)

        self_width = 600
        self_height = 600
        self.geometry(f"{self_width}x{self_height}")
        self.title("Research Tool - Figure")
        self.configure(bg="#EEEEEE")

        self.plot(data, keywords)

        self.resizable(True, True)

    def plot(self, data, keywords):
        figure = Figure()
        plt = figure.add_subplot(1, 1, 1)

        for keyword in keywords:
            plt.plot(data.index, data[keyword], label=keyword)
        plt.legend()
        canvas = FigureCanvasTkAgg(figure, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0)
