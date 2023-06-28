from import_logic import ctypes
from ui.window_ui import tk
from import_logic import lib



def listbox_1_used(event):
    global unit_in
    unit_in = ctypes.c_char_p(listbox_1.get(listbox_1.curselection()).encode())

def listbox_2_used(event):
    global unit_out
    unit_out = ctypes.c_char_p(listbox_2.get(listbox_2.curselection()).encode())

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



val_entry = tk.Entry()
val_entry.grid(column=1, row=0)

def on_button_click():
    val = ctypes.c_double(float(val_entry.get()))
    result = lib.convert_SI(val, unit_in, unit_out)
    result_var.set(result)

button = tk.Button(text="Convert", command=on_button_click)
button.grid(column=1, row=1)

result_var = tk.StringVar()
result_entry = tk.Entry(textvariable=result_var, state="readonly")
result_entry.grid(column=1, row=2)


