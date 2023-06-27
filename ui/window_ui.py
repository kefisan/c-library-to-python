import tkinter as tk
from tkinter import END

root = tk.Tk()
root.title("Unit Calculator")
root.geometry("1000x500")

# Text area
entry = tk.Entry()
entry.grid(column=1, row=0, sticky='N')
entry.insert(END, 'Choose values:')

#Listbox







"""
todo:

fix listbox2 +
bind function to listbox
add output
design
"""