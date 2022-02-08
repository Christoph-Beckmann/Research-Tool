import gui_settings
from tkinter import Tk, Canvas, Text, Button, PhotoImage, filedialog
import tkinter.ttk


def open_textfile(entry: Text):
    filetypes = (
        ('AlL files', '*.*')
    )
    file = filedialog.askopenfilename(
        filetypes=[filetypes],
        defaultextension=".txt")
    fob = open(file, 'r')
    text = fob.read()
    entry.delete(1.0, tkinter.END)
    entry.insert(tkinter.INSERT, text)
    fob.close()


def open_gui_summarize():

    form_summarize = Tk()
    form_summarize.title("Research Tool - Summarize")

    form_summarize_width = 1200
    form_summarize_height = 800

    center_x, center_y = gui_settings.center_form(form_summarize, form_summarize_width, form_summarize_height)
    form_summarize.geometry(f'{form_summarize_width}x{form_summarize_height}+{center_x}+{center_y}')

    form_summarize.configure(bg="#EEEEEE")

    canvas = Canvas(
        form_summarize,
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
    btn_image_summarize = PhotoImage(
        file=gui_settings.assets("btn_summarize.png"))
    btn_summarize = Button(
        image=btn_image_summarize,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    btn_summarize.place(
        x=200.0,
        y=716.0,
        width=200.0,
        height=58.0
    )

    btn_image_export = PhotoImage(
        file=gui_settings.assets("btn_export.png"))
    btn_export = Button(
        image=btn_image_export,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    btn_export.place(
        x=800.0,
        y=716.0,
        width=200.0,
        height=58.0
    )

    btn_image_pathpicker = PhotoImage(
        file=gui_settings.assets("btn_pathpicker.png"))
    btn_pathpicker = Button(
        image=btn_image_pathpicker,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_textfile(entry_text),
        relief="flat"
    )
    btn_pathpicker.place(
        x=50.0,
        y=716.0,
        width=65.0,
        height=58.0
    )

    btn_image_back = PhotoImage(
        file=gui_settings.assets("btn_back.png"))
    btn_back = Button(
        image=btn_image_back,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Back clicked"),
        relief="flat"
    )
    btn_back.place(
        x=0.0,
        y=0.0,
        width=65.0,
        height=58.0
    )

    entry_image_text = PhotoImage(
        file=gui_settings.assets("entry_text.png"))
    entry_text = canvas.create_image(
        300.0,
        381.0,
        image=entry_image_text
    )
    entry_text = Text(
        bd=0,
        fg='#EEEEEE',
        bg="#00ADB5",
        highlightthickness=0
    )
    entry_text.place(
        x=50.0,
        y=79.0,
        width=500.0,
        height=602.0
    )

    entry_image_summarized = PhotoImage(
        file=gui_settings.assets("entry_summarized.png"))
    entry_summarized = canvas.create_image(
        900.0,
        381.0,
        image=entry_image_summarized
    )
    entry_summarized = Text(
        bd=0,
        fg='#222831',
        bg="#EEEEEE",
        highlightthickness=0
    )
    entry_summarized.place(
        x=650.0,
        y=79.0,
        width=500.0,
        height=602.0
    )

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
        text="Summarized Text:",
        fill="#EEEEEE",
        font=("Roboto", 36 * -1)
    )

    form_summarize.resizable(False, False)
    form_summarize.mainloop()
