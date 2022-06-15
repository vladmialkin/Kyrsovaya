import tkinter as tk
from Tree import Tree


class Interface(tk.Tk):
    """класс основного интерфейса программы"""
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Interface, cls).__new__(cls)
        return cls.__instance

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

        self.tree_list_label = tk.Label(self.panel_label, text="0/0", width=14)
        self.tree_list_label.place(x=20, y=370)

        self.forward_button = tk.Button(self.panel_label, text="->", width=5)
        self.forward_button.place(x=80, y=400)

        self.back_button = tk.Button(self.panel_label, text="<-", width=5)
        self.back_button.place(x=20, y=400)

        self.tree_label = tk.Label(self, width=600, height=30)
        self.tree_label.place(x=300, y=10)

        self.tree = Tree(self.tree_label, self.redmine)

    def get_projects(self):
        """функция вывода проектов"""
        projects = self.redmine.get_projects_all()
        self.tree.init_columns("Проект")
        self.tree.insert_tree(projects)
        self.tree.check_tree_list(projects)
        self.tree_list_label.config(text=f"1/{self.tree.list + 1}")

    def get_trackers(self):
        """функция вывода трекеров"""
        trackers = self.redmine.get_projects_all()
        self.tree.init_columns("Трекер")
        self.tree.insert_tree(trackers)
        self.tree.check_tree_list(trackers)
        self.tree_list_label.config(text=f"1/{self.tree.list + 1}")

    def get_issues(self):
        """функция вывода задач"""
        issues = self.redmine.get_issues_all()
        self.tree.init_columns("Задача")
        self.tree.insert_tree(issues)
        self.tree.check_tree_list(issues)
        self.tree_list_label.config(text=f"1/{self.tree.list + 1}")

    def get_users(self):
        """функция вывода пользователей"""
        users = self.redmine.get_users_all()
        self.tree.init_columns("Пользователь")
        self.tree.insert_tree(users)
        self.tree.check_tree_list(users)
        self.tree_list_label.config(text=f"1/{self.tree.list + 1}")
