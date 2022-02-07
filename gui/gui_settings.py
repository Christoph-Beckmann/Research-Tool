from pathlib import Path
from tkinter import Tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Center given Tkinter Form on the Screen
def center_form(form: Tk, form_width: int, form_height: int):
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()

    x_coordinate = (screen_width / 2) - (form_width / 2)
    y_coordinate = (screen_height / 2) - (form_height / 2)

    return int(x_coordinate), int(y_coordinate)
