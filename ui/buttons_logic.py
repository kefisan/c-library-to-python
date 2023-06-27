from import_logic import ctypes
from ui.window_ui import tk

unit_in = ctypes.c_char_p(b"yard")
unit_out = ctypes.c_char_p(b"cm")

def listbox_1_used(event):
    print(listbox_1.get(listbox_1.curselection()))

listbox_1 = tk.Listbox(height=8)
options = ["mm", "cm", "m", "km", "mile", "yard", "foot", "inch"]
for item in options:
    listbox_1.insert(options.index(item), item)
listbox_1.bind("<<ListboxSelect>>", listbox_1_used)
listbox_1.grid(column=0, row=0)

def listbox_2_used(event):
    # Gets current selection from listbox_1
    print(listbox_2.get(listbox_2.curselection()))

listbox_2 = tk.Listbox(height=8)
options2 = ["mm", "cm", "m", "km", "mile", "yard", "foot", "inch"]
for item in options2:
    listbox_2.insert(options2.index(item), item)
listbox_2.bind("<<ListboxSelect>>", listbox_2_used)
listbox_2.grid(column=2, row=0)