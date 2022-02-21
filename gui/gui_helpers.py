import sys
import logging
import tkinter
from pathlib import Path
import tkinter as tk
from tkinter import filedialog as fd
import csv
from researchtool import keywordsanalytics

logger = logging.getLogger(__name__)

PROJECT_DIR = Path(__file__).parents[1]
sys.path.append(str(PROJECT_DIR / Path("./researchtool")))  # System Path of backend is included - really necessary?


# Relative Asset Path
def assets(path: str) -> Path:

    return PROJECT_DIR / Path("./gui/assets") / Path(path)


# Center given Tkinter Form on the Screen with the help from stackoverflow:
# https://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter/10018670#10018670
def center_form(form: tk, form_width: int, form_height: int):

    form.update_idletasks()
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (form_width / 2)
    y_coordinate = (screen_height / 2) - (form_height / 2)

    return int(x_coordinate), int(y_coordinate)


# Listbox Operations

def insert_kw(listbox: tkinter.Listbox, keywords):
    s = 0
    for i in keywords:
        listbox.insert(s, i[0])
        s += 1


def insert_related_kw(listbox: tkinter.Listbox, selection):
    keywords = keywordsanalytics.related_keywords(selection)
    listbox.delete(0, tk.END)
    s = 0
    for i in keywords:
        listbox.insert(s, i)
        s += 1


def get_selection(listbox: tkinter.Listbox):
    selection_list = [listbox.get(i) for i in listbox.curselection()]

    return selection_list


def change_state(button: tk.Button) -> None:
    print("normal")
    if button.config(state=tk.DISABLED):
        print("normalized")
        button["state"] = tk.NORMAL
    else:
        button["state"] = tk.NORMAL


# File Dialogs

# Summary - Open Textfile
def open_textfile(textarea: tk.Text):
    try:
        file = fd.askopenfilename(
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
            defaultextension=".txt")
        if file is None:
            return
        else:
            with open(file, "r") as f:
                text = f.read()
            textarea.delete(1.0, tk.END)
            textarea.insert(tk.INSERT, text)
    except Exception as error:
        logger.error(error)


# Summary - Export Summary
def export_textarea(textarea: tk.Text):
    try:
        file = fd.asksaveasfilename(
            initialfile="Untitled.txt",
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
            defaultextension=".txt"
        )
        if file is None:
            return
        else:
            text = str(textarea.get(1.0, tk.END))
            with open(file, "w") as file:
                file.write(text)
    except Exception as error:
        logger.error(error)


# Analysis - Export extracted keywords
def export_kw_listbox(listbox: tk.Listbox):
    try:
        csvfile = fd.asksaveasfilename(
            initialfile="Untitled.csv",
            filetypes=[("All Files", "*.*"), ("CSV", "*.csv")],
            defaultextension=".csv"
        )
        if csvfile is None:
            return
        else:
            items = listbox.get(0, tk.END)
            items = ("Keywords", ) + items
            with open(csvfile, "w", newline="") as csvfile:
                writer = csv.writer(csvfile, delimiter="\n")
                writer.writerow(items)
    except Exception as error:
        logger.error(error)


# Analysis - Export further related keywords
def export_further_listbox(listbox_kw: tk.Listbox, listbox_further: tk.Listbox):
    try:
        csvfile = fd.asksaveasfilename(
            initialfile="Untitled.csv",
            filetypes=[("All Files", "*.*"), ("CSV", "*.csv")],
            defaultextension=".csv"
        )
        if csvfile is None:
            return
        else:
            items = listbox_further.get(0, tk.END)
            current_selection = listbox_kw.get(listbox_kw.curselection())
            items = (f"{current_selection}", ) + items
            with open(csvfile, "w", newline="") as csvfile:
                writer = csv.writer(csvfile, delimiter="\n")
                writer.writerow(items)
    except Exception as error:
        logger.error(error)


# Close Window Function
def close_window(self):
    self.destroy()
