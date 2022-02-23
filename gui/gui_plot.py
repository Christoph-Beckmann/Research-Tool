import logging
import tkinter as tk
from gui.gui_helpers import center_form
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

logger = logging.getLogger(__name__)


class GUIPlot(tk.Toplevel):
    """
    Class for create the GUI Plot
    """
    def __init__(self, parent, data, keywords):
        """
        Constructor for GUIPlot class

        :param data: DataFrame from :function: `~researchtool.keywordanalytics.interest_of_time`
        :param keywords: list of selected related keywords
        """
        super().__init__(parent)

        self_width = 600
        self_height = 600
        center_x, center_y = center_form(self, self_width, self_height)  # Get center coordinates
        self.geometry(f"{self_width}x{self_height}+{center_x}+{center_y}")
        self.title("Research Tool - Figure")
        self.configure(bg="#EEEEEE")

        self.plot(data, keywords)

        self.resizable(True, True)

    def plot(self, data, keywords):
        """
        Function to plot data: y: Date, x: keywords with relative occurrence to top related keyword.

        :param data: DataFrame from :function: `~researchtool.keywordanalytics.interest_of_time`
        :param keywords: list of selected related keywords
        """
        figure = Figure()
        plt = figure.add_subplot(1, 1, 1)

        for keyword in keywords:
            plt.plot(data.index, data[keyword], label=keyword)
        plt.legend()
        canvas = FigureCanvasTkAgg(figure, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0)
