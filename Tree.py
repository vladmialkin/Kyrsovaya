import tkinter as tk
from tkinter import ttk


class Tree(ttk.Treeview):
    """класс таблицы интерфейса"""
    def __init__(self, tree_label, redmine):
        super().__init__()
        self.tree_label = tree_label
        self.redmine = redmine
        self.tree = ttk.Treeview(self.tree_label, show="headings", height=30)
        self.tree["columns"] = ["1"]
        self.tree.column("1", width=500)
        self.tree.place(x=0, y=0)
        self.list = 1
        self.list_current = 1
        self.forward_id = 0
        self.back_id = 0
        self.data_resource = []

    def init_columns(self, list_columns):
        """функция создает колонки таблицы"""
        self.tree = ttk.Treeview(self.tree_label, show="headings", height=30)
        self.tree["columns"] = list_columns
        for column in list_columns:
            self.tree.column(column, width=600, minwidth=100, stretch=tk.NO)
            self.tree.heading(column, text=column)
        self.tree.place(x=0, y=0)

    def check_tree_list(self, resource):
        """функция ищет количество страниц таблицы"""
        count = 0
        self.data_resource = []
        self.list_current = 1

        for val in resource:
            self.data_resource.append(val)
            count += 1
        if count % 21 == 0:
            self.list = int(count / 21)
        else:
            self.list = int(count / 21) + 1
