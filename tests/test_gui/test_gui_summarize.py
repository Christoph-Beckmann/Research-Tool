import test_gui_settings
from tkinter import Button, PhotoImage, filedialog
import tkinter.ttk


def open_textfile(textbox: tkinter.Text):
    filetypes = (
        ('AlL files', '*.*')
    )
    file = tkinter.filedialog.askopenfilename(
        filetypes=[filetypes],
        defaultextension=".txt")
    fob = open(file, 'r')
    text = fob.read()
    textbox.delete(1.0, tk.END)
    textbox.insert(tk.INSERT, text)
    fob.close()


class GUISummarize(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
    
        self_width = 1200
        self_height = 800
    
        center_x, center_y = test_gui_settings.center_form(self, self_width, self_height)
        self.geometry(f'{self_width}x{self_height}+{center_x}+{center_y}')

        self.title("Research Tool - Summarize")
        self.configure(bg="#EEEEEE")
    
        canvas = tkinter.Canvas(
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
        btn_image_summarize = tkinter.PhotoImage(
            file=test_gui_settings.assets("btn_summarize.png"))
        btn_summarize = tkinter.Button(
            image=btn_image_summarize,
            command=lambda: print("Summarize clicked"),
        )
        btn_summarize.place(
            x=200.0,
            y=716.0,
            width=200.0,
            height=58.0
        )

        btn_image_export = PhotoImage(
            file=test_gui_settings.assets("btn_export.png"))
        btn_export = Button(
            image=btn_image_export,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Export pressed"),
            relief="flat"
        )
        btn_export.place(
            x=800.0,
            y=716.0,
            width=200.0,
            height=58.0
        )

        btn_image_pathpicker = PhotoImage(
            file=test_gui_settings.assets("btn_pathpicker.png"))
        btn_pathpicker = Button(
            image=btn_image_pathpicker,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: open_textfile(textbox_text),
            relief="flat"
        )
        btn_pathpicker.place(
            x=50.0,
            y=716.0,
            width=65.0,
            height=58.0
        )
    
        btn_image_back = tkinter.PhotoImage(
            file=test_gui_settings.assets("btn_back.png"))
        btn_back = ttkinter.Button(
            image=btn_image_back,
            command=lambda: self.closewindow(),
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
    
        textbox_text = tkinter.Text(
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
    
        textbox_summarized = tkinter.Text(
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
    
        self.resizable(False, False)

    def closewindow(self):
        self.destroy()
