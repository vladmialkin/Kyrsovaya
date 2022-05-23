import os.path
import tkinter as tk
from tkinter import ttk


class Authorization(tk.Tk):
    """Класс интерфейса программы"""
    __inctance = None

    def __new__(cls, *args, **kwargs):
        if cls.__inctance is None:
            cls.__inctance = super(Authorization, cls).__new__(cls)
        return cls.__inctance

    def __init__(self):
        super().__init__()
        self.geometry("240x240")
        self.title("Авторизация")

        self.__login = tk.StringVar()
        self.__password = tk.StringVar()
        self.error_text = tk.StringVar()

        self.save_var = tk.BooleanVar()
        self.save_var.set(False)

        self.login_entry = ttk.Entry(self, width=20, textvariable=self.__login)
        self.login_entry.place(x=5, y=5)

        self.password_entry = ttk.Entry(self, width=20, textvariable=self.__password, show='*')
        self.password_entry.place(x=5, y=35)

        self.error_label = tk.Label(self, width=20, textvariable=self.error_text)
        self.error_label.place(x=5, y=60)

        self.save_data_button = tk.Checkbutton(self, text="Сохранить логин и пароль", variable=self.save_var, onvalue=1,
                                               offvalue=0)
        self.save_data_button.place(x=5, y=90)

        self.auth_button = tk.Button(self, width=20, text="OK")
        self.auth_button.place(x=40, y=160)

        self.bind("<Return>", self.callback)
        self.check_data()

    def check_save(self):
        """функция проверяет согласие на сохранение логина и пароля"""
        if self.save_var.get() is True:
            self.save()
        else:
            if os.path.exists("local_settings.py") is True:
                os.remove("local_settings.py")

    def save(self):
        """функция сохраняет логин и пароль"""
        file = open("local_settings.py", "w")
        file.write(f"save_flag = {True} \n")
        file.write(f"login={self.__login.get()} \n")
        file.write(f"password={self.__password.get()} \n")


