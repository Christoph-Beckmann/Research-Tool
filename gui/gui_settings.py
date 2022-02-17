import sys
from pathlib import Path
import tkinter as tk
from tkinter import filedialog as fd

PROJECT_DIR = Path(__file__).parents[1]
sys.path.append(str(PROJECT_DIR / Path('./researchtool')))  # System Path of backend is included - really necessary?


def assets(path: str) -> Path:
    return PROJECT_DIR / Path('./gui/assets') / Path(path)


# Center given Tkinter Form on the Screen with the help from stackoverflow:
# https://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter/10018670#10018670
def center_form(form: tk, form_width: int, form_height: int):

    form.update_idletasks()
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()

    x_coordinate = (screen_width / 2) - (form_width / 2)
    y_coordinate = (screen_height / 2) - (form_height / 2)

    return int(x_coordinate), int(y_coordinate)


def filetypes_dialogs():
    filetypes = \
        ("All Files", "*.*"), \
        ("Text Documents", "*.txt")
    return filetypes


def open_textfile(textarea: tk.Text):
    file = fd.askopenfilename(
        filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')],
        defaultextension=".txt")
    if file is None:
        return
    fob = open(file, 'r')
    text = fob.read()
    textarea.delete(1.0, tk.END)
    textarea.insert(tk.INSERT, text)
    fob.close()


def export_textfile(textarea: tk.Text):
    file = fd.asksaveasfilename(
        initialfile='Untitled.txt',
        filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')],
        defaultextension=".txt")
    if file is None:
        return
    text = str(textarea.get(1.0, tk.END)
               )
    with open(file, 'w') as file:
        file.write(text)


def is_top_empty(textarea: tk.Entry):
    if len(textarea.get()) == 0:
        topn = 5                            # Standard value
    else:
        topn = int(textarea.get())
    return topn


def clear_textarea(textarea: tk.Text):
    textarea.delete('1.0', tk.END)


def close_window(self):
    self.destroy()
