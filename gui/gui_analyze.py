import logging
import tkinter as tk
from gui import gui_helpers
from gui import gui_plot
from researchtool import keywordsanalytics

logger = logging.getLogger(__name__)


class GUIAnalyze(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self_width = 1200
        self_height = 800

        center_x, center_y = gui_helpers.center_form(self, self_width, self_height)
        self.geometry(f"{self_width}x{self_height}+{center_x}+{center_y}")
        self.title("Research Tool - Keywords Analysis")
        self.configure(bg="#EEEEEE")

        # Build Canvas

        canvas = tk.Canvas(
            self,
            bg="#EEEEEE",
            height=800,
            width=1200,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)

        canvas.create_rectangle(
            600.0,
            0.0,
            1200.0,
            800.0,
            fill="#00ADB5",
            outline="")

        # Labels

        canvas.create_text(
            207.0,
            17.0,
            anchor="nw",
            text="Insert Text:",
            fill="#222831",
            font=("Roboto", 36 * -1)
        )
        canvas.create_text(
            752.0,
            17.0,
            anchor="nw",
            text="Analyze Keywords",
            fill="#EEEEEE",
            font=("Roboto", 36 * -1)
        )
        canvas.create_text(
            215.0,
            496.0,
            anchor="nw",
            text="Max Word Count:",
            fill="#000000",
            font=("Roboto", 24 * -1)
        )
        canvas.create_text(
            215.0,
            573.0,
            anchor="nw",
            text="Duplication Threshold:",
            fill="#000000",
            font=("Roboto", 24 * -1)
        )
        canvas.create_text(
            215.0,
            652.0,
            anchor="nw",
            text="Max Keywords:",
            fill="#000000",
            font=("Roboto", 24 * -1)
        )

        # TextArea

        textarea_text = tk.Text(
            self,
            bd=0,
            fg="#EEEEEE",
            bg="#00ADB5",
            highlightthickness=0
        )
        textarea_text.place(
            x=50.0,
            y=79.0,
            width=500.0,
            height=377.0
        )

        # List Boxes

        listbox_keywords = tk.Listbox(
            self,
            bd=0,
            bg="#EEEEEE",
            highlightthickness=0,
        )
        listbox_keywords.place(
            x=650.0,
            y=79.0,
            width=249.0,
            height=377.0
        )

        # adapted:
        # https://stackoverflow.com/questions/7616541/get-selected-item-in-listbox-and-call-another-function-storing-the-selected-for
        def on_select_listbox_kw(event):
            try:
                widget = event.widget
                selection_item = widget.curselection()
                selection = widget.get(selection_item[0])
                gui_helpers.insert_related_kw(listbox_further_keywords, selection)
            except Exception as error:
                logger.error(error)

        listbox_keywords.bind(
            "<<ListboxSelect>>",
            on_select_listbox_kw
        )

        listbox_further_keywords = tk.Listbox(
            self,
            bd=0,
            bg="#EEEEEE",
            highlightthickness=0,
            selectmode="multiple"
        )
        listbox_further_keywords.place(
            x=901.0,
            y=79.0,
            width=249.0,
            height=377.0
        )

        # Spin-boxes
        spinbox_wordcount = tk.Spinbox(
            self,
            justify="center",
            bd=0,
            fg="#EEEEEE",
            bg="#00ADB5",
            highlightthickness=0,
            font=("Roboto", 24 * -1),
            from_=1,
            to=20,
        )
        spinbox_wordcount.place(
            x=475.0,
            y=481.0,
            width=75.0,
            height=56.0
        )

        spinbox_duplication = tk.Spinbox(
            self,
            justify="center",
            bd=0,
            fg="#EEEEEE",
            bg="#00ADB5",
            highlightthickness=0,
            font=("Roboto", 24 * -1),
            format="%.2f",
            increment=0.1,
            from_=0.1,
            to=0.99,
        )
        spinbox_duplication.place(
            x=475.0,
            y=558.0,
            width=75.0,
            height=56.0
        )

        spinbox_max_keywords = tk.Spinbox(
            self,
            justify="center",
            bd=0,
            fg="#EEEEEE",
            bg="#00ADB5",
            highlightthickness=0,
            font=("Roboto", 24 * -1),
            from_=1,
            to=100
        )
        spinbox_max_keywords.place(
            x=475.0,
            y=637.0,
            width=75.0,
            height=56.0
        )

        # Dropdown
        clicked = tk.StringVar()
        clicked.set("today 5-y")
        dropdown = tk.OptionMenu(
            self,
            clicked,
            "today 5-y",
            "today 12-m",
            "today 3-m",
            "today 1-m",
        )
        dropdown.place(
            x=1040.0,
            y=580.0,
            width=110.0,
        )

        # Buttons

        self.btn_image_analyze_kw = tk.PhotoImage(
            file=gui_helpers.assets("btn_analyze_keywords.png"))
        btn_analyze_kw = tk.Button(
            self,
            image=self.btn_image_analyze_kw,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (
                listbox_keywords.delete(0, tk.END),
                gui_helpers.insert_kw(
                    listbox_keywords,
                    keywordsanalytics.extract_keywords(
                        textarea_text.get(1.0, tk.END),
                        int(spinbox_wordcount.get()),
                        float(spinbox_duplication.get()),
                        int(spinbox_max_keywords.get()),
                    )
                )
            ),
            relief="flat"
        )
        btn_analyze_kw.place(
            x=215.0,
            y=716.0,
            width=335.0,
            height=58.0
        )

        self.btn_image_pathpicker = tk.PhotoImage(
            file=gui_helpers.assets("btn_pathpicker.png"))
        btn_pathpicker = tk.Button(
            self,
            image=self.btn_image_pathpicker,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: gui_helpers.open_textfile(textarea_text),
            relief="flat"
        )
        btn_pathpicker.place(
            x=50.0,
            y=473.0,
            width=65.0,
            height=58.0
        )

        self.btn_image_export = tk.PhotoImage(
            file=gui_helpers.assets("btn_export.png"))
        btn_export_kw = tk.Button(
            self,
            image=self.btn_image_export,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: gui_helpers.export_further_listbox(listbox_keywords, listbox_further_keywords),
            relief="flat"
        )
        btn_export_kw.place(
            x=918.9,
            y=481.0,
            width=200.0,
            height=58.0
        )
        btn_export_further_kw = tk.Button(
            self,
            image=self.btn_image_export,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: gui_helpers.export_kw_listbox(listbox_keywords),
            relief="flat"
        )
        btn_export_further_kw.place(
            x=681.1,
            y=481.0,
            width=200.0,
            height=58.0
        )

        self.btn_image_get_historical = tk.PhotoImage(
            file=gui_helpers.assets("btn_get_historical.png"))
        btn_get_historical = tk.Button(
            self,
            image=self.btn_image_get_historical,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_gui_plot(
                gui_helpers.get_selection(listbox_further_keywords),  # Get list of selected listbox Items
                clicked.get()  # Dropdown selected Item: Timeframe
            ),
            relief="flat"
        )
        btn_get_historical.place(
            x=650.0,
            y=566.0,
            width=365.0,
            height=59.0
        )

        self.btn_image_back = tk.PhotoImage(
            file=gui_helpers.assets("btn_back.png"))
        btn_back = tk.Button(
            self,
            image=self.btn_image_back,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: gui_helpers.close_window(self),
            relief="flat"
        )
        btn_back.place(
            x=0.0,
            y=0.0,
            width=65.0,
            height=58.0
        )

        self.resizable(False, False)

    def open_gui_plot(self, list_sel, dropdown_sel):
        form_plot = gui_plot.GUIPlot(
            self,
            keywordsanalytics.interest_of_time(
                list_sel,
                dropdown_sel
            ),
            list_sel
        )
        form_plot.grab_set()

