import tkinter as tk
from pytrends.request import TrendReq
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)


class GUIPlot(tk.Toplevel):
    def __init__(self, parent, data, keywords):
        super().__init__(parent)

        self_width = 500
        self_height = 500
        self.geometry(f"{self_width}x{self_height}")
        self.title("Research Tool - Figure")
        self.configure(bg="#EEEEEE")

        self.plot(data, keywords)

        self.resizable(False, False)

    def plot(self, data, keywords):
        figure = Figure()
        plt = figure.add_subplot(1, 1, 1)

        for keyword in keywords:
            plt.plot(data.index, data[keyword], label=keyword)
        plt.legend()
        canvas = FigureCanvasTkAgg(figure, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0)


class GUIAnalyze(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self_width = 1200
        self_height = 800

        self.geometry(f"{self_width}x{self_height}")
        self.title("Research Tool - Keyword Analysis")
        self.configure(bg="#EEEEEE")

        btn_get_historical = tk.Button(
            self,
            borderwidth=0,
            highlightthickness=0,
            bg="#00ADB5",
            command=lambda: (
                GUIPlot(
                    self,
                    self.interest_of_time(
                        ["Python"],
                        "today 5-y"
                    ),
                    ["Python"]
                )
            ),
            relief="flat"
        )
        btn_get_historical.place(
            x=650.0,
            y=566.0,
            width=365.0,
            height=59.0
        )

    def interest_of_time(self, keyword_list, timeframe):
        trend = TrendReq()
        keywords = keyword_list
        trend.build_payload(kw_list=keywords, cat=None, timeframe=timeframe, geo="")
        data = trend.interest_over_time()

        return data


class GUIMainMenu(tk.Tk):
    def __init__(self):
        super().__init__()

        self_width = 800
        self_height = 500
        self.geometry(f"{self_width}x{self_height}")
        self.title("Research Tool")
        self.configure(bg="#EEEEEE")

        btn_analyze = tk.Button(
            self,
            borderwidth=0,
            bg="#00ADB5",
            highlightthickness=0,
            command=lambda: self.open_gui_analyze(),
            relief="flat"
        )

        btn_analyze.place(
            x=500.0,
            y=288.0,
            width=200.0,
            height=58.0
        )

    def open_gui_analyze(self):
        form_analyze = GUIAnalyze(self)
        form_analyze.grab_set()


if __name__ == "__main__":
    mainmenu = GUIMainMenu()
    mainmenu.mainloop()
