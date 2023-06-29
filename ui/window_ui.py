import tkinter as tk

root = tk.Tk()
root.option_add("*Font", "TkDefaultFont 24")
root.title("Unit Calculator")
root.geometry("910x350")

# Text area
label = tk.Label(text='Choose values:')
label.grid(column=1, row=0, sticky='N')