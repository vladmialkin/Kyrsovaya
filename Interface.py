import tkinter as tk
from Tree import Treeview


class Interface(tk.Tk):
    """ класс основного графического интерфейса """
    def __init__(self, redmine):
        super().__init__()
        self.projects = None
        self.trackers = None
        self.issues = None
        self.users = None
        self.value = None

        self.search_variable = tk.StringVar()

        self.redmine = redmine

        self.panel_label = tk.Label(self, width=40, height=30, background="#34A2FE")
        self.panel_label.place(x=10, y=10)

        self.tracker_button = tk.Button(self.panel_label, text="Список трекеров", width=30, command=self.get_trackers)
        self.tracker_button.place(x=20, y=20)

        self.projects_button = tk.Button(self.panel_label, text="Список проектов", width=30, command=self.get_projects)
        self.projects_button.place(x=20, y=50)

        self.upload_button = tk.Button(self.panel_label, text="Список пользователей", width=30, command=self.get_users)
        self.upload_button.place(x=20, y=80)

        self.tree_label = tk.Label(self, width=600, height=30)
        self.tree_label.place(x=300, y=10)

        self.tree = Treeview(self.tree_label, self.redmine)

        self.issues_button = tk.Button(self.panel_label, text="Список задач", width=30, command=self.get_issues)
        self.issues_button.place(x=20, y=110)

        self.search_tree_entry = tk.Entry(self.panel_label, width=36, textvariable=self.search_variable)
        self.search_tree_entry.place(x=20, y=140)

        self.search_tree_button = tk.Button(self.panel_label, text='Поиск', width=30, command=self.get_search)
        self.search_tree_button.place(x=20, y=165)

        self.tree_list_label = tk.Label(self.panel_label, text="0/0", width=14)
        self.tree_list_label.place(x=20, y=370)

        self.forward_tree_button = tk.Button(self.panel_label, text="->", width=5, command=lambda: (
            self.tree.forward_insert(), self.tree_list_label.config(text=f"{self.tree.list_current}/{self.tree.list}")))

        self.forward_tree_button.place(x=80, y=400)

        self.back_tree_button = tk.Button(self.panel_label, text="<-", width=5, command=lambda: (
            self.tree.back_insert(), self.tree_list_label.config(text=f"{self.tree.list_current}/{self.tree.list}")))

        self.back_tree_button.place(x=20, y=400)

    def insert_date_tree(self, variable):
        """функция заполняет данные в таблицу"""
        self.tree.insert_tree(variable)

    def change(self, variable):
        """функция запонляет данные в таблицу, проверяет количество страниц"""
        self.insert_date_tree(variable)
        self.tree.check_tree_list(variable)
        self.tree_list_label.config(text=f"1/{self.tree.list}")

    def get_projects(self):
        """функция получает проекты"""
        self.projects = self.redmine.get_projects_all()
        self.tree.init_columns("Проект")
        self.change(self.projects)

    def get_trackers(self):
        """функция получает трекеры"""
        self.trackers = self.redmine.get_trackers_all()
        self.tree.init_columns("Трекер")
        self.change(self.trackers)

    def get_issues(self):
        """функция получает задачи"""
        self.issues = self.redmine.get_issues_all()
        self.tree.init_columns("Задача")
        self.change(self.issues)

    def get_users(self):
        """функция получает пользователей"""
        self.users = self.redmine.get_users_all()
        self.tree.init_columns("Пользователь")
        self.change(self.users)

    def get_search(self):
        self.value = self.search_tree_entry.get()
        self.tree.get_search_tree(self.value)

