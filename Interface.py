import tkinter as tk


class Interface(tk.Tk):
    """класс основного интерфейса программы"""
    __inctance = None

    def __new__(cls, *args, **kwargs):
        if cls.__inctance is None:
            cls.__inctance= super(Interface, cls).__new__(cls)
        return cls.__inctance

    def __init__(self, redmine):
        super().__init__()
        self.redmine = redmine

        self.panel_label = tk.Label(self, width=40, height=30, background="#34A2FE")
        self.panel_label.place(x=10, y=10)

        self.tracker_button = tk.Button(self.panel_label, text="Список трекеров", width=30)
        self.tracker_button.place(x=20, y=20)

        self.project_button = tk.Button(self.panel_label, text="Список проектов", width=30)
        self.project_button.place(x=20, y=50)

        self.issue_button = tk.Button(self.panel_label, text="Список задач", width=30)
        self.issue_button.place(x=20, y=80)

        self.user_button = tk.Button(self.panel_label, text="Список пользователей", width=30)
        self.user_button.place(x=20, y=110)

        self.forward_button = tk.Button(self.panel_label, text="->", width=5)
        self.forward_button.place(x=80, y=400)

        self.back_button = tk.Button(self.panel_label, text="<-", width=5)
        self.back_button.place(x=20, y=400)

