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
            text="Duplication Treshold:",
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
            fg='#EEEEEE',
            bg="#00ADB5",
            highlightthickness=0
        )
        textarea_text.place(
            x=50.0,
            y=79.0,
            width=500.0,
            height=377.0
        )

        # Listbox

        listbox_keywords = tk.Listbox(
            self,
            bd=0,
            bg="#EEEEEE",
            highlightthickness=0,
            selectmode="multiple"
        )
        listbox_keywords.place(
            x=650.0,
            y=79.0,
            width=500.0,
            height=377.0
        )

        # Entry's

        entry_wordcount = tk.Entry(
            self,
            justify="center",
            bd=0,
            fg="#EEEEEE",
            bg="#00ADB5",
            highlightthickness=0,
            font=("Roboto", 24 * -1),
        )
        entry_wordcount.place(
            x=485.0,
            y=481.0,
            width=65.0,
            height=56.0
        )

        entry_duplication = tk.Entry(
            self,
            justify="center",
            bd=0,
            fg="#EEEEEE",
            bg="#00ADB5",
            highlightthickness=0,
            font=("Roboto", 24 * -1),
        )
        entry_duplication.place(
            x=485.0,
            y=558.0,
            width=65.0,
            height=56.0
        )

        entry_max_keywords = tk.Entry(
            self,
            justify="center",
            bd=0,
            fg="#EEEEEE",
            bg="#00ADB5",
            highlightthickness=0,
            font=("Roboto", 24 * -1),
        )
        entry_max_keywords.place(
            x=485.0,
            y=637.0,
            width=65.0,
            height=56.0
        )

        # Buttons

        self.btn_image_analyze_kw = tk.PhotoImage(
            file=gui_settings.assets("btn_analyze_kw.png"))
        btn_analyze_kw = tk.Button(
            self,
            image=self.btn_image_analyze_kw,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (
                listbox_keywords.delete(0, tk.END),
                keywordsanalytics.extract_keywords(
                    textarea_text.get(1.0, tk.END),
                    1,
                    0.2,
                    20,
                    listbox_keywords
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
            file=gui_settings.assets("btn_pathpicker.png"))
        btn_pathpicker = tk.Button(
            self,
            image=self.btn_image_pathpicker,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: gui_settings.open_textfile(textarea_text),
            relief="flat"
        )
        btn_pathpicker.place(
            x=50.0,
            y=473.0,
            width=65.0,
            height=58.0
        )

        self.btn_image_export = tk.PhotoImage(
            file=gui_settings.assets("btn_export.png"))
        btn_export = tk.Button(
            self,
            image=self.btn_image_export,
            borderwidth=0,
            highlightthickness=0,
           # command=lambda: gui_settings.export_textfile(textarea_keywords),
            relief="flat"
        )
        btn_export.place(
            x=950.0,
            y=481.0,
            width=200.0,
            height=58.0
        )

        self.btn_image_back = tk.PhotoImage(
            file=gui_settings.assets("btn_back.png"))
        btn_back = tk.Button(
            self,
            image=self.btn_image_back,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: gui_settings.close_window(self),
            relief="flat"
        )
        btn_back.place(
            x=0.0,
            y=0.0,
            width=65.0,
            height=58.0
        )

        self.resizable(False, False)