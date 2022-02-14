import tkinter
import test_gui_settings
import test_gui_summarize

# With help from this side: https://www.pythontutorial.net/tkinter/tkinter-toplevel/


class GUIMainMenu(tkinter.Toplevel):
    def __init__(self):
        super().__init__(self)

        self_width = 800
        self_height = 500
        
        # center_x, center_y = test_gui_settings.center_form(self, self_width, self_height)
        # self.geometry(f'{self_width}x{self_height}+{center_x}+{center_y}')
        self.geometry(f'{self_width}x{self_height}')
        self.title("Research Tool")
        self.configure(bg="#EEEEEE")

        # Background Canvas

        canvas = tkinter.Canvas(
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
        
        # Title, Description (Texts) and Images on Left Side
        
        canvas.create_text(
            50.0,
            56.0,
            anchor="nw",
            text="Research Tool",
            fill="#EEEEEE",
            font=("Roboto", 48 * -1)
        )
        
        image_checkbox = tkinter.PhotoImage(
            file=test_gui_settings.assets("checkbox.png"))
        
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
        
        btn_image_Summarize = tkinter.PhotoImage(
            file=test_gui_settings.assets("btn_Summarize.png"))
        
        btn_Summarize = tkinter.Button(
            image=btn_image_Summarize,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_gui_summarize(),
            relief="flat"
        )
        btn_Summarize.place(
            x=500.0,
            y=197.0,
            width=200.0,
            height=58.0
        )
        
        btn_image_Analyze = tkinter.PhotoImage(
            file=test_gui_settings.assets("btn_Analyze.png"))
        
        btn_Analyze = tkinter.Button(
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
        
        btn_image_Research = tkinter.PhotoImage(
            file=test_gui_settings.assets("btn_Research.png"))
        
        btn_Research = tkinter.Button(
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

        self.resizable(False, False)

    def open_gui_summarize(self):
        gui_summarize = test_gui_summarize.GUISummarize(self)
        gui_summarize.grab_set()


if __name__ == "__main__":
    mainmenu = GUIMainMenu()
    mainmenu.mainloop()
