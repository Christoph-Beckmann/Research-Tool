import gui_settings
from tkinter import Tk, Canvas, Button, PhotoImage


form_mainmenu = Tk()
form_mainmenu.title("Research Tool")

form_mainmenu_width = 800
form_mainmenu_height = 500

x, y = gui_settings.center_form(form_mainmenu, form_mainmenu_width, form_mainmenu_height)
form_mainmenu.geometry(f'{form_mainmenu_width}x{form_mainmenu_height}+{x}+{y}')

form_mainmenu.configure(bg="#EEEEEE")

# functions to open new windows

# Background Canvas

canvas = Canvas(
    form_mainmenu,
    bg="#EEEEEE",
    height=500,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    400.0,
    500.0,
    fill="#00ADB5",
    outline="")

# Title, Description (Texts) and Images on Left Side

canvas.create_text(
    50.0,
    56.0,
    anchor="nw",
    text="Research Tool",
    fill="#EEEEEE",
    font=("Roboto", 48 * -1)
)

image_checkbox = PhotoImage(
    file=gui_settings.relative_to_assets("checkbox.png"))

image_cb1 = canvas.create_image(
    96.0,
    208.0,
    image=image_checkbox
)

image_cb2 = canvas.create_image(
    96.0,
    273.0,
    image=image_checkbox
)

image_cb3 = canvas.create_image(
    96.0,
    340.0,
    image=image_checkbox
)

image_cb4 = canvas.create_image(
    96.0,
    406.0,
    image=image_checkbox
)

canvas.create_text(
    125.0,
    194.0,
    anchor="nw",
    text="Summarize Text",
    fill="#FFFFFF",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    125.0,
    324.0,
    anchor="nw",
    text="Analyze Keywords",
    fill="#FFFFFF",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    125.0,
    257.0,
    anchor="nw",
    text="Identify Keywords",
    fill="#FFFFFF",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    125.0,
    390.0,
    anchor="nw",
    text="Further Research",
    fill="#FFFFFF",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    7.0,
    481.0,
    anchor="nw",
    text="©  (2022) Christoph Beckmann",
    fill="#FFFFFF",
    font=("Roboto", 12 * -1)
)

# Right Side: Subtitle and Buttons

canvas.create_text(
    415.0,
    66.0,
    anchor="nw",
    text="What should be done?",
    fill="#222831",
    font=("Roboto", 36 * -1)
)

# Buttons

btn_image_Summarize = PhotoImage(
    file=gui_settings.relative_to_assets("btn_Summarize.png"))

btn_Summarize = Button(
    image=btn_image_Summarize,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Summarize pressed"),
    relief="flat"
)
btn_Summarize.place(
    x=500.0,
    y=197.0,
    width=200.0,
    height=58.0
)

btn_image_Analyze = PhotoImage(
    file=gui_settings.relative_to_assets("btn_Analyze.png"))

btn_Analyze = Button(
    image=btn_image_Analyze,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Analyze pressed"),
    relief="flat"
)

btn_Analyze.place(
    x=500.0,
    y=288.0,
    width=200.0,
    height=58.0
)

btn_image_Research = PhotoImage(
    file=gui_settings.relative_to_assets("btn_Research.png"))

btn_Research = Button(
    image=btn_image_Research,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Research pressed"),
    relief="flat"
)
btn_Research.place(
    x=500.0,
    y=379.0,
    width=200.0,
    height=58.0
)

form_mainmenu.resizable(False, False)

form_mainmenu.mainloop()
