import tkinter as tk
from tkinter import filedialog as fd
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
        canvas.create_rectangle(
            600.0,
            0.0,
            1200.0,
            800.0,
            fill="#00ADB5",
            outline="")
        self.btn_image_summarize = tk.PhotoImage(
            file=gui_settings.assets("btn_summarize.png"))
        btn_summarize = tk.Button(
            self,
            image=self.btn_image_summarize,
            command=lambda: textbox_summarized.insert(
                tk.END,
                str(self.open_summary(textbox_text)))
        )
        btn_summarize.place(
            x=200.0,
            y=716.0,
            width=200.0,
            height=58.0
        )

        self.btn_image_export = tk.PhotoImage(
            file=gui_settings.assets("btn_export.png"))
        btn_export = tk.Button(
            self,
            image=self.btn_image_export,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.export_textfile(textbox_summarized),
            relief="flat"
        )
        btn_export.place(
            x=800.0,
            y=716.0,
            width=200.0,
            height=58.0
        )

        self.btn_image_back = tk.PhotoImage(
            file=gui_settings.assets("btn_back.png"))
        btn_back = tk.Button(
            self,
            image=self.btn_image_back,
            command=lambda: self.close_window()
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
            file=gui_settings.assets("btn_pathpicker.png"))
        btn_pathpicker = tk.Button(
            self,
            image=self.btn_image_pathpicker,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_textfile(textbox_text),
            relief="flat"
        )
        btn_pathpicker.place(
            x=50.0,
            y=716.0,
            width=65.0,
            height=58.0
        )
    
        self.resizable(False, False)

    def open_textfile(self, textbox: tk.Text):
        filetypes = (
            ('AlL files', '*.*')
        )
        file = fd.askopenfilename(
            filetypes=[filetypes],
            defaultextension=".txt")
        fob = open(file, 'r')
        text = fob.read()
        textbox.delete(1.0, tk.END)
        textbox.insert(tk.INSERT, text)
        fob.close()

    def open_summary(self, textbox: tk.Text):
        summary = ". ".join(summarization.build_summary((textbox.get(1.0, tk.END), 1)))
        return summary

    def export_textfile(self, textbox: tk.Text):
        filetypes = (
            ('AlL files', '*.*')
        )
        file = fd.asksaveasfilename(
            initialfile='Untitled.txt',
            defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file is None:
            return
        text = str(textbox.get(1.0, tk.END))
        with open(file, 'w') as file:
            file.write(text)

    def close_window(self):
        self.destroy()
