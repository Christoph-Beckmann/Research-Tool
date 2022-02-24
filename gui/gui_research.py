import logging
import tkinter as tk
from tkinter import ttk
import gui_helpers
from gui import gui_helpers as helper
from helpers import detectlanguage
from researchtool.research import scrape
import webbrowser as web

logger = logging.getLogger(__name__)


class GUIResearch(tk.Toplevel):
    """
    Class for create Research Form
    """
    def __init__(self, parent):
        """
        Constructor for GUIResearch Class
        """
        super().__init__(parent)

        self_width = 1800
        self_height = 400

        center_x, center_y = helper.center_form(self, self_width, self_height)
        self.geometry(f"{self_width}x{self_height}+{center_x}+{center_y}")
        self.title("Research Tool - Research")
        self.configure(bg="#EEEEEE")

        canvas = tk.Canvas(
            self,
            bg="#00ADB5",
            height=400,
            width=1800,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        keys = ("title", "publication_info", "snippet", "title_link")
        tree = ttk.Treeview(self, columns=keys, show="headings")

        # Entry Query Search

        entry_query = tk.Entry(
            self,
            bd=0,
            bg="#EEEEEE",
            highlightthickness=0,
            font=("Roboto", 24 * -1),
        )
        entry_query.place(
            x=47.0,
            y=278.0,
            width=414.0,
            height=56.0
        )

        # Buttons

        # Button Search
        canvas.place(x=0, y=0)
        self.btn_img_search = tk.PhotoImage(
            file=helper.assets("btn_search.png"))
        btn_search = tk.Button(
            self,
            image=self.btn_img_search,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:  self.create_tree(tree, entry_query.get()),
            relief="flat"
        )
        btn_search.place(
            x=505.0,
            y=278.0,
            width=274.0,
            height=59.0
        )

        # Button Open Link
        self.btn_img_open_link = tk.PhotoImage(
            file=helper.assets("btn_open_link.png"))
        btn_open_link = tk.Button(
            self,
            image=self.btn_img_open_link,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: web.open(self.selected_item(tree)),
            relief="flat"
        )
        btn_open_link.place(
            x=1020.0,
            y=278.0,
            width=274.0,
            height=59.0
        )

        # Button Back
        self.btn_img_back = tk.PhotoImage(
            file=helper.assets("btn_back.png"))
        btn_back = tk.Button(
            self,
            image=self.btn_img_back,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: gui_helpers.close_window(self),
            relief="flat"
        )
        btn_back.place(
            x=867.0,
            y=336.0,
            width=65.0,
            height=58.0
        )

        self.resizable(False, False)

    @staticmethod
    def create_tree(tree, query):
        """

        :param tree: Which TreeView Widget?
        :param query: Search Query --> Entry Text
        :return tree: Return tree widget
        """
        tree.heading("title", text="Title")
        tree.heading("publication_info", text="Publication")
        tree.heading("snippet", text="Snippet")
        tree.heading("title_link", text="Title Link")
        tree.column("title", width=600, anchor=tk.W)
        tree.column("publication_info", width=200, anchor=tk.W)
        tree.column("snippet", width=500, anchor=tk.W)
        tree.column("title_link", width=500, anchor=tk.W)

        query = query
        data = scrape(
            query,
            detectlanguage(query, True)
        )
        keys = ("title", "publication_info", "snippet", "title_link")

        for dictionary in data:                   # Join List of Dictionaries and insert needed data into TreeView
            tree_values = []
            for key in keys:
                tree_values.append(dictionary[key])
            tree.insert("", tk.END, values=tuple(tree_values))

        tree.grid(row=0, column=0, sticky="nsew")

        return tree

    @staticmethod
    def selected_item(tree: ttk.Treeview):
        """
        Get Link from selected row

        :param tree: Which TreeView Widget
        :return link: Return just the link of current item
        """
        cur_item = tree.focus()
        tuple_item = tree.item(cur_item, "values")
        link = tuple_item[len(tuple_item)-1]
        return link
