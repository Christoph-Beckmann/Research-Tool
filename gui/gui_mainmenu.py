import logging
import tkinter as tk
from gui import gui_summarize
from gui import gui_helpers as helper
from gui import gui_analyze
from gui import gui_research

logger = logging.getLogger(__name__)


class GUIMainMenu(tk.Tk):
    """
    Class for create the main Form
    """
    def __init__(self):
        """
        Constructor for GUIMainMenu class
        """
        super().__init__()

        self_width = 800
        self_height = 500

        center_x, center_y = helper.center_form(self, self_width, self_height)     # Get center coordinates
        self.geometry(f"{self_width}x{self_height}+{center_x}+{center_y}")
        self.title("Research Tool")
        self.configure(bg="#EEEEEE")

        # *Build Canvas*

        canvas = tk.Canvas(
            self,
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
        
        # *Title, Description (Texts) and Images on Left Side*
        
        canvas.create_text(
            50.0,
            56.0,
            anchor="nw",
            text="Research Tool",
            fill="#EEEEEE",
            font=("Roboto", 48 * -1)
        )
        
        self.image_checkbox = tk.PhotoImage(
            file=helper.assets("img_checkbox.png")
        )

        canvas.create_image(
            96.0,
            208.0,
            image=self.image_checkbox
        )
        
        canvas.create_image(
            96.0,
            273.0,
            image=self.image_checkbox
        )
        
        canvas.create_image(
            96.0,
            340.0,
            image=self.image_checkbox
        )
        canvas.create_image(
            96.0,
            406.0,
            image=self.image_checkbox

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
        
        # *Buttons*

        # Summarized
        self.btn_image_Summarize = tk.PhotoImage(
            file=helper.assets("btn_Summarize.png")
        )
        
        btn_summarize = tk.Button(
            self,
            image=self.btn_image_Summarize,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_gui_summarize(),
            relief="flat"
        )
        btn_summarize.place(
            x=500.0,
            y=197.0,
            width=200.0,
            height=58.0
        )

        # Keyword Analysis
        self.btn_image_Analyze = tk.PhotoImage(
            file=helper.assets("btn_Analyze.png")
        )
        btn_analyze = tk.Button(
            self,
            image=self.btn_image_Analyze,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_gui_analyze(),
            relief="flat"
        )
        
        btn_analyze.place(
            x=500.0,
            y=288.0,
            width=200.0,
            height=58.0
        )

        # Further Research
        self.btn_image_Research = tk.PhotoImage(
            file=helper.assets("btn_Research.png")
        )

        btn_research = tk.Button(
            self,
            image=self.btn_image_Research,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_gui_research(),
            relief="flat"
        )
        btn_research.place(
            x=500.0,
            y=379.0,
            width=200.0,
            height=58.0
        )

        self.btn_image_exit = tk.PhotoImage(
            file=helper.assets("btn_back.png"))

        # Close Form
        btn_exit = tk.Button(
            self,
            image=self.btn_image_exit,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: helper.close_window(self),
            relief="flat"
        )
        btn_exit.place(
            x=367.0,
            y=442.0,
            width=65.0,
            height=58.0
        )

        self.resizable(False, False)

    # Functions to call TopLevel Windows

    def open_gui_summarize(self):
        """
        Function to open TopLevel GUI Summarize
        """
        form_summarize = gui_summarize.GUISummarize(self)
        form_summarize.grab_set()

    def open_gui_analyze(self):
        """
        Function to open TopLevel GUI Analyze
        """
        form_analyze = gui_analyze.GUIAnalyze(self)
        form_analyze.grab_set()

    def open_gui_research(self):
        """
        Function to open TopLevel GUI Research
        """
        form_research = gui_research.GUIResearch(self)
        form_research.grab_set()


########################################################################################################################


if __name__ == "__main__":
    # Set special variables. Python interpreter reads this first.
    # Prevent parts of code from being run when the modules are imported.
    # To get a deeper insight I used logging Package for debug, info and warning messages.
    import logging.config
    logging_config = helper.PROJECT_DIR / "logging.conf"
    logging.config.fileConfig(logging_config, disable_existing_loggers=False)

    # Create Class
    mainmenu = GUIMainMenu()
    mainmenu.mainloop()
