from import_logic import ctypes
from ui.window_ui import tk

unit_in_label = tk.Label(text="Unit in:")
unit_in_label.grid(column=0, row=1)

unit_out_label = tk.Label(text="Unit out:")
unit_out_label.grid(column=2, row=1)

def listbox_1_used(event):
    global unit_in
    if listbox_1.curselection():
        unit_in = ctypes.c_char_p(listbox_1.get(listbox_1.curselection()).encode())
        unit_in_label["text"] = f"Unit in: {listbox_1.get(listbox_1.curselection())}"

def listbox_2_used(event):
    global unit_out
    if listbox_2.curselection():
        unit_out = ctypes.c_char_p(listbox_2.get(listbox_2.curselection()).encode())
        unit_out_label["text"] = f"Unit out: {listbox_2.get(listbox_2.curselection())}"

listbox_1 = tk.Listbox(height=8)
options = ["mm", "cm", "m", "km", "mile", "yard", "foot", "inch"]
for item in options:
    listbox_1.insert(options.index(item), item)
listbox_1.bind("<<ListboxSelect>>", listbox_1_used)
listbox_1.grid(column=0, row=0)

listbox_2 = tk.Listbox(height=8)
options2 = ["mm", "cm", "m", "km", "mile", "yard", "foot", "inch"]
for item in options2:
    listbox_2.insert(options2.index(item), item)
listbox_2.bind("<<ListboxSelect>>", listbox_2_used)
listbox_2.grid(column=2, row=0)
