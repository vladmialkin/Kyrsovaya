import tkinter as tk


class Interface(tk.Tk):
    """класс основного интерфейса программы"""
    __inctance = None

    def __new__(cls, *args, **kwargs):
        if cls.__inctance is None:
            cls.__inctance= super(RedmineApi, cls).__new__(cls)
        return cls.__inctance

    def __init__(self, redmine):
        super().__init__()
        self.redmine = redmine

        self.panel_label = tk.Label(self, width=40, height=30, background="#34A2FE")
        self.panel_label.place(x=10, y=10)
