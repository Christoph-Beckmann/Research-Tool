from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Research Tool")

# Center Tkinter Window on the Screen

window_width = 800
window_height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

window.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

window.geometry("800x500")
window.configure(bg="#EEEEEE")


canvas = Canvas(
    window,
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

canvas.create_text(
    7.0,
    481.0,
    anchor="nw",
    text="©  (2022) Christoph Beckmann",
    fill="#FFFFFF",
    font=("Roboto", 12 * -1)
)

image_checkbox = PhotoImage(
    file=relative_to_assets("checkbox.png"))
image_cb1 = canvas.create_image(
    58.0,
    408.0,
    image=image_checkbox
)

image_cb2 = canvas.create_image(
    58.0,
    341.0,
    image=image_checkbox
)

image_cb3 = canvas.create_image(
    58.0,
    274.0,
    image=image_checkbox
)

image_cb4 = canvas.create_image(
    58.0,
    208.0,
    image=image_checkbox
)

canvas.create_text(
    85.0,
    392.0,
    anchor="nw",
    text="Further Research",
    fill="#FFFFFF",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    85.0,
    325.0,
    anchor="nw",
    text="Analyze Keywords",
    fill="#FFFFFF",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    85.0,
    258.0,
    anchor="nw",
    text="Identify Keywords",
    fill="#FFFFFF",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    85.0,
    194.0,
    anchor="nw",
    text="Summarize Text",
    fill="#FFFFFF",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    50.0,
    56.0,
    anchor="nw",
    text="Research Tool",
    fill="#EEEEEE",
    font=("Roboto", 48 * -1)
)

# Buttons

btn_image_Summarize = PhotoImage(
    file=relative_to_assets("btn_Summarize.png"))

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
    file=relative_to_assets("btn_Analyze.png"))

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
    file=relative_to_assets("btn_Research.png"))

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

canvas.create_text(
    415.0,
    66.0,
    anchor="nw",
    text="What should be done?",
    fill="#222831",
    font=("Roboto", 36 * -1)
)

window.resizable(False, False)

window.mainloop()
