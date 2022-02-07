import tkinter

import gui_settings
from tkinter import Tk, Canvas, Text, Button, PhotoImage, filedialog


form_summarize = Tk()

form_summarize_width = 1200
form_summarize_height = 800

x, y = gui_settings.center_form(form_summarize, form_summarize_width, form_summarize_height)
form_summarize.geometry(f'{form_summarize_width}x{form_summarize_height}+{x}+{y}')

form_summarize.configure(bg="#EEEEEE")


def open_textfile():
    filetypes = (
        ('AlL files', '*.*')
    )
    file = filedialog.askopenfilename(
        filetypes=[filetypes],
        defaultextension=".txt")
    fob = open(file, 'r')
    text = fob.read()
    entry_text.delete(1.0, tkinter.END)
    entry_text.insert(tkinter.INSERT, text)
    fob.close()


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

btn_image_Summarize = PhotoImage(
    file=gui_settings.relative_to_assets("btn_summarize.png"))
btn_Summarize = Button(
    image=btn_image_Summarize,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
btn_Summarize.place(
    x=200.0,
    y=716.0,
    width=200.0,
    height=58.0
)

btn_image_Export = PhotoImage(
    file=gui_settings.relative_to_assets("btn_export.png"))
btn_Export = Button(
    image=btn_image_Export,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
btn_Export.place(
    x=800.0,
    y=716.0,
    width=200.0,
    height=58.0
)

btn_image_pathpicker = PhotoImage(
    file=gui_settings.relative_to_assets("btn_pathpicker.png"))
btn_pathpicker = Button(
    image=btn_image_pathpicker,
    borderwidth=0,
    highlightthickness=0,
    command=open_textfile,
    relief="flat"
)
btn_pathpicker.place(
    x=50.0,
    y=716.0,
    width=65.0,
    height=58.0
)

btn_image_back = PhotoImage(
    file=gui_settings.relative_to_assets("btn_back.png"))
btn_back = Button(
    image=btn_image_back,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
btn_back.place(
    x=0.0,
    y=0.0,
    width=65.0,
    height=58.0
)

entry_image_text = PhotoImage(
    file=gui_settings.relative_to_assets("entry_text.png"))
entry_bg_text = canvas.create_image(
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
    file=gui_settings.relative_to_assets("entry_summarized.png"))
entry_bg_summarized = canvas.create_image(
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
