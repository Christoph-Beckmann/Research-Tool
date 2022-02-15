import tkinter as tk
from gui import gui_settings
from researchtool import summarization


class GUISummarize(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self_width = 1200
        self_height = 800

        center_x, center_y = gui_settings.center_form(self, self_width, self_height)
        self.geometry(f'{self_width}x{self_height}+{center_x}+{center_y}')
        self.title("Research Tool - Summarize")
        self.configure(bg="#EEEEEE")

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

        canvas.create_text(
            202.0,
            731.0,
            anchor="nw",
            text="Top:",
            fill="#000000",
            font=("Roboto", 24 * -1)
        )

        textbox_top = tk.Entry(
            self,
            justify="center",
            bd=0,
            fg="#EEEEEE",
            bg="#00ADB5",
            highlightthickness=0,
            font=("Roboto", 24 * -1),
        )
        textbox_top.place(
            x=267.0,
            y=716.0,
            width=65.0,
            height=56.0
        )
        canvas.create_rectangle(
            600.0,
            0.0,
            1200.0,
            800.0,
            fill="#00ADB5",
            outline="")
        self.btn_image_summarize = tk.PhotoImage(
            file=gui_settings.assets("btn_summarize.png")
        )
        btn_summarize = tk.Button(
            self,
            image=self.btn_image_summarize,
            command=lambda: (
                textbox_summarized.delete(1.0, tk.END),
                textbox_summarized.insert(
                    1.0,
                    ". ".join(
                        summarization.build_summary(
                            textbox_text.get(1.0, tk.END),
                            gui_settings.is_top_empty(textbox_top)
                        )
                    )
                )
            )
        )
        btn_summarize.place(
            x=350.0,
            y=716.0,
            width=200.0,
            height=58.0
        )

        self.btn_image_export = tk.PhotoImage(
            file=gui_settings.assets("btn_export.png")
        )
        btn_export = tk.Button(
            self,
            image=self.btn_image_export,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: gui_settings.export_textfile(textbox_summarized),
            relief="flat"
        )
        btn_export.place(
            x=948.0,
            y=716.0,
            width=200.0,
            height=58.0
        )

        self.btn_image_analyze_kw = tk.PhotoImage(
            file=gui_settings.assets("btn_analyzekw.png"))
        btn_analyze_kw = tk.Button(
            self,
            image=self.btn_image_analyze_kw,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Analyze Keywords pressed"),
            relief="flat"
        )
        btn_analyze_kw.place(
            x=649.0,
            y=716.0,
            width=200.0,
            height=58.0
        )

        self.btn_image_back = tk.PhotoImage(
            file=gui_settings.assets("btn_back.png")
        )
        btn_back = tk.Button(
            self,
            image=self.btn_image_back,
            command=lambda: gui_settings.close_window(self)
        )
        btn_back.place(
            x=0.0,
            y=0.0,
            width=65.0,
            height=58.0
        )

        canvas.create_text(
            207.0,
            17.0,
            anchor="nw",
            text="Insert Text:",
            fill="#222831",
            font=("Roboto", 36 * -1)
        )

        textbox_text = tk.Text(
            self,
            bd=0,
            fg='#EEEEEE',
            bg="#00ADB5",
            highlightthickness=0
        )
        textbox_text.place(
            x=50.0,
            y=79.0,
            width=500.0,
            height=602.0
        )

        canvas.create_text(
            752.0,
            17.0,
            anchor="nw",
            text="Summarized Text:",
            fill="#EEEEEE",
            font=("Roboto", 36 * -1)
        )

        textbox_summarized = tk.Text(
            self,
            bd=0,
            fg='#222831',
            bg="#EEEEEE",
            highlightthickness=0
        )
        textbox_summarized.place(
            x=650.0,
            y=79.0,
            width=500.0,
            height=602.0
        )

        self.btn_image_pathpicker = tk.PhotoImage(
            file=gui_settings.assets("btn_pathpicker.png")
        )
        btn_pathpicker = tk.Button(
            self,
            image=self.btn_image_pathpicker,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: gui_settings.open_textfile(textbox_text),
            relief="flat"
        )
        btn_pathpicker.place(
            x=50.0,
            y=716.0,
            width=65.0,
            height=58.0
        )
    
        self.resizable(False, False)
