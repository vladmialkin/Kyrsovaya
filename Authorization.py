import os.path
import tkinter as tk
from tkinter import ttk
from RedmineApi import RedmineApi
from Interface import Interface


class Authorization(tk.Tk):
    """Класс интерфейса программы"""
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Authorization, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        super().__init__()
        self.geometry("260x240")
        self.title("Авторизация")

        self.__login = tk.StringVar()
        self.__password = tk.StringVar()
        self.error_text = tk.StringVar()

        self.save_var = tk.BooleanVar()
        self.save_var.set(False)

        self.redmine = RedmineApi(self.error_text)
        self.new_window = None

        self.login_entry = ttk.Entry(self, width=20, textvariable=self.__login)
        self.login_entry.place(x=5, y=5)

        self.password_entry = ttk.Entry(self, width=20, textvariable=self.__password, show='*')
        self.password_entry.place(x=5, y=35)

        self.error_label = tk.Label(self, width=35, textvariable=self.error_text)
        self.error_label.place(x=5, y=60)

        self.save_data_button = tk.Checkbutton(self, text="Сохранить логин и пароль", variable=self.save_var, onvalue=1,
                                               offvalue=0)
        self.save_data_button.place(x=5, y=90)

        self.auth_button = tk.Button(self, width=20, text="OK",
                                     command=lambda: (self.redmine_authorization(), self.check_save()))
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
        file.write(f"login='{self.__login.get()}' \n")
        file.write(f"password='{self.__password.get()}' \n")

    def check_data(self):
        """функция проверяет на наличие сохраненного логина и пароля"""
        if os.path.exists("local_settings.py") is True:
            from local_settings import save_flag, login, password
            self.save_var.set(save_flag)
            self.__login.set(f"{login}")
            self.__password.set(f"{password}")

    def redmine_authorization(self):
        """функция авторизуется в Redmine и выводит основной интерфейс"""
        if self.__login.get() != "" and self.__password.get() != "":
            self.redmine.connecting(self.__login.get(), self.__password.get())
            try:
                if self.redmine.connection and self.redmine.redmine.auth():
                    self.new_window = Interface(self.redmine)
                    self.new_window.geometry("1024x720")
                    self.new_window.title("Василий")
                    self.destroy()
            except Exception as e:
                print(e)
                self.error_text.set("Неверно введен логин/пароль")
        else:
            self.error_text.set("Поле логин/пароль не может быть пустым")

    def callback(self, event):
        """функция вызова горячей клавиши при входе"""
        self.redmine_authorization()
