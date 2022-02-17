import tkinter as tk
from tkinter import filedialog as fd
from gui import gui_settings
from researchtool import keywordsanalytics


class GUIAnalyze(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self_width = 1200
        self_height = 800

        center_x, center_y = gui_settings.center_form(self, self_width, self_height)
        self.geometry(f'{self_width}x{self_height}+{center_x}+{center_y}')
        self.title("Research Tool - Keywords Analysis")
        self.configure(bg="#EEEEEE")

        self.resizable(False, False)
