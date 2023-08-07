# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 00:04:43 2023

@author: Ranadip.Dey
"""
import csv
import tkinter as tk
from tkinter import ttk


class PropertyAppearance:
    def __init__(self, root):
        self.root = root
        self.root.title("Property Data App")
        
        self.tree = ttk.Treeview(root, columns=("ID", "Address", "Bedrooms", "Bathrooms", "Rent",  "Status"))
        self.tree.heading("#1", text="ID")
        self.tree.heading("#2", text="Address")
        self.tree.heading("#3", text="Bedrooms")
        self.tree.heading("#4", text="Bathrooms")
        self.tree.heading("#5", text="Rent")
        self.tree.heading("#6", text="Status")
        self.tree.pack()

        self.load_data()


    def load_data(self):
        with open("property_data.csv", mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.tree.insert("", "end", values=(row["property_id"], row["address"], row["num_bedrooms"], row["num_bathrooms"],  row["monthly_rent"],  row["status"]))

if __name__ == "__main__":
    root = tk.Tk()
    app = PropertyAppearance(root)
    root.mainloop()