import sys
from pathlib import Path
import tkinter as tk

PROJECT_DIR = Path(__file__).parents[1]
sys.path.append(str(PROJECT_DIR / Path('./researchtool')))  # System Path of backend is included - really necessary?


def assets(path: str) -> Path:
    return PROJECT_DIR / Path('./gui/assets') / Path(path)


# Center given Tkinter Form on the Screen
def center_form(form: tk, form_width: int, form_height: int):
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()

    x_coordinate = (screen_width / 2) - (form_width / 2)
    y_coordinate = (screen_height / 2) - (form_height / 2)

    return int(x_coordinate), int(y_coordinate)
