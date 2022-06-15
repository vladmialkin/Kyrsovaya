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

    def init_columns(self, list_columns):
        """функция создает колонки таблицы"""
        self.tree = ttk.Treeview(self.tree_label, show="headings", height=30)
        self.tree["columns"] = list_columns
        for column in list_columns:
            self.tree.column(column, width=600, minwidth=100, stretch=tk.NO)
            self.tree.heading(column, text=column)
        self.tree.place(x=0, y=0)