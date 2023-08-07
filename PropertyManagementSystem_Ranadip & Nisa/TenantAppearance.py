# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 00:29:23 2023

@author: Ranadip.Dey
"""

import csv
import tkinter as tk
from tkinter import ttk

class TenantAppearance:
    def __init__(self, root):
        self.root = root
        self.root.title("Tenant Data App")
        
        self.tree = ttk.Treeview(root, columns=("Tenant ID", "Name", "Contact Phone", "Contact Email", "Property ID"))
        self.tree.heading("#1", text="Tenant ID")
        self.tree.heading("#2", text="Name")
        self.tree.heading("#3", text="Contact Phone")
        self.tree.heading("#3", text="Contact Email")
        self.tree.heading("#4", text="Property ID")
        self.tree.pack()

        self.load_data()

    def load_data(self):
        with open("tenants_data.csv", mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.tree.insert("", "end", values=(row["Tenant ID"], row["Name"], row["Contact Phone"], row["Contact Email"],  row["Property ID"]))

if __name__ == "__main__":
    root = tk.Tk()
    app = TenantAppearance(root)
    root.mainloop()
