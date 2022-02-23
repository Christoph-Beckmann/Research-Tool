import logging
import sys
from pathlib import Path
import tkinter as tk
from tkinter import filedialog as fd
import csv
from researchtool import keywordsanalytics

#Do not “from nearby_module import function”
# Do “my package.nearby_module import function”


logger = logging.getLogger(__name__)

########################################################################################################################
# Basic Functions

PROJECT_DIR = Path(__file__).parents[1]  # Relative Project Dir path
sys.path.append(str(PROJECT_DIR / Path("./researchtool")))  # System Path of functions is included


def assets(path: str) -> Path:
    """
    :param path: Asset file name
    :return: relative asset path
    """
    return PROJECT_DIR / Path("./gui/assets") / Path(path)


def center_form(form: tk, form_width: int, form_height: int):
    """
    Center given Tkinter Form on the Screen with the help from stackoverflow:
    https://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter/10018670#10018670

    :param form: Tkinter Form
    :param form_width: given width of specific form
    :param form_height: given height of specific form

    :return x_coordinate: calculated x coordinate for centering
    :return y_coordinate: calculated y coordinate for centering
    """
    form.update_idletasks()
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (form_width / 2)
    y_coordinate = (screen_height / 2) - (form_height / 2)

    return int(x_coordinate), int(y_coordinate)


def close_window(self):
    """
    Function to destroy the tk Window
    """
    self.destroy()

########################################################################################################################
# Listbox Functions

def insert_kw(listbox: tk.Listbox, keywords):
    """
    Insert list of keywords into given listbox

    :param listbox: Given Listbox Widget
    :param keywords: Given Keywords List from :modul: `keywordanalytics.extract_keywords`
    """
    listbox.delete(0, tk.END)
    s = 0
    for i in keywords:
        listbox.insert(s, i[0])
        s += 1


def insert_related_kw(listbox: tk.Listbox, keywords):
    """
    Insert list of related keywords from selection into second listbox

    :param listbox: listbox in which related keywords should be pasted
    :param keywords: selected keywords in listbox keywords
    """

    listbox.delete(0, tk.END)
    s = 0
    for i in keywords:
        listbox.insert(s, i)
        s += 1


def get_selection(listbox: tk.Listbox):
    """
    Get list of selected related keywords

    :param listbox: Which Listbox Widget
    :return: List of selected related keywords
    """
    selection_list = [listbox.get(i) for i in listbox.curselection()]

    return selection_list

########################################################################################################################
# File Dialogs


def open_textfile(textarea: tk.Text):
    """
    Open Dialog Function to get text from a textfile and paste it into the summary textbox
    :param textarea: In which textarea should the text be pasted? --> Summary textbox
    :raises Exception: Get error message, i.e. File wasn't selected
    """
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


def export_textarea(textarea: tk.Text):
    """
    Open Dialog Function to export summarized text from textbox into textfile.
    :param textarea: In which textarea is the text stored? --> textarea_text
    :raises Exception: Get error message, i.e. File wasn't created
    """
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


def export_kw_listbox(listbox: tk.Listbox):
    """
    Open Dialog Function to export extracted keywords from listbox into csv.
    :param listbox: Which listbox? -> listbox_keywords
    :raises Exception: Get error message, i.e. File wasn't created
    """
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
            items = ("Keywords",) + items
            with open(csvfile, "w", newline="") as csvfile:
                writer = csv.writer(csvfile, delimiter="\n")
                writer.writerow(items)
    except Exception as error:
        logger.error(error)


def export_further_listbox(listbox_kw: tk.Listbox, listbox_further: tk.Listbox):
    """
    Open Dialog Function to selected keyword and via Google API determined related keywords
    :param listbox_kw: Which listbox? -> listbox_keywords
    :param listbox_further: Which listbox? -> listbox_further_keywords
    :raises Exception: Get error message, i.e. File wasn't created
    """
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
            items = (f"{current_selection}",) + items
            with open(csvfile, "w", newline="") as csvfile:
                writer = csv.writer(csvfile, delimiter="\n")
                writer.writerow(items)
    except Exception as error:
        logger.error(error)
