import tkinter as tk


class Authorization(tk.Tk):
    """Класс интерфейса программы"""
    __inctance = None

    def __new__(cls, *args, **kwargs):
        if cls.__inctance is None:
            cls.__inctance= super(Authorization, cls).__new__(cls)
        return cls.__inctance

    def __init__(self):
        super().__init__()
        self.geometry("240x240")
        self.title("Авторизация")

