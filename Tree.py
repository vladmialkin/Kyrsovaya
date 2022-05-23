import tkinter as tk
from tkinter import ttk


class Tree(tk.Tk):
    """класс таблицы интерфейса"""
    def __init__(self, tree_label, redmine):
        super().__init__()
        self.redmine = redmine
        self.tree = ttk.Treeview(tree_label, show="headings", height=30)
        self.tree["columns"] = ["1"]
        self.tree.column("1", width=500)
        self.tree.place(x=0, y=0)

