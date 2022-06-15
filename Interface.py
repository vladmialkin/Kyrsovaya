import tkinter as tk
from Tree import Tree


columns_1 = ["Трекер"]
columns_2 = ["Проект"]
columns_3 = ["Задача"]
columns_4 = ["Пользователь"]

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

        self.tracker_button = tk.Button(self.panel_label, text="Список трекеров", width=30, command=self.get_trackers)
        self.tracker_button.place(x=20, y=20)

        self.project_button = tk.Button(self.panel_label, text="Список проектов", width=30, command=self.get_projects)
        self.project_button.place(x=20, y=50)

        self.issue_button = tk.Button(self.panel_label, text="Список задач", width=30, command=self.get_issues)
        self.issue_button.place(x=20, y=80)

        self.user_button = tk.Button(self.panel_label, text="Список пользователей", width=30, command=self.get_users)
        self.user_button.place(x=20, y=110)

        self.tree_list_label = tk.Label(self.panel_label, text="0/0", width=14)
        self.tree_list_label.place(x=20, y=370)

        self.forward_button = tk.Button(self.panel_label, text="->", width=5,
                                        command=lambda: (self.tree.forward_insert(),
                                                         self.tree_list_label.config(
                                                             text=f"{self.tree.list_current}/{self.tree.list}"),))
        self.forward_button.place(x=80, y=400)

        self.back_button = tk.Button(self.panel_label, text="<-", width=5,
                                     command=lambda: (self.tree.back_insert(),
                                                      self.tree_list_label.config(
                                                          text=f"{self.tree.list_current}/{self.tree.list}"),))
        self.back_button.place(x=20, y=400)

        self.tree_label = tk.Label(self, width=600, height=30)
        self.tree_label.place(x=300, y=10)

        self.tree = Tree(self.tree_label, self.redmine)

    def get_projects(self):
        """функция вывода проектов"""
        projects = self.redmine.get_projects_all()
        self.tree.init_columns(columns_2)
        self.tree.insert_tree(projects)
        self.tree.check_tree_list(projects)
        self.tree_list_label.config(text=f"1/{self.tree.list + 1}")

    def get_trackers(self):
        """функция вывода трекеров"""
        trackers = self.redmine.get_trackers_all()
        self.tree.init_columns(columns_1)
        self.tree.insert_tree(trackers)
        self.tree.check_tree_list(trackers)
        self.tree_list_label.config(text=f"1/{self.tree.list + 1}")

    def get_issues(self):
        """функция вывода задач"""
        issues = self.redmine.get_issues_all()
        self.tree.init_columns(columns_3)
        self.tree.insert_tree(issues)
        self.tree.check_tree_list(issues)
        self.tree_list_label.config(text=f"1/{self.tree.list + 1}")

    def get_users(self):
        """функция вывода пользователей"""
        users = self.redmine.get_users_all()
        self.tree.init_columns(columns_4)
        self.tree.insert_tree(users)
        self.tree.check_tree_list(users)
        self.tree_list_label.config(text=f"1/{self.tree.list + 1}")
