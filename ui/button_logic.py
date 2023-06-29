from import_logic import ctypes, lib
from ui.window_ui import tk
import ui.lists as l

val_entry = tk.Entry()
val_entry.grid(column=1, row=0)


def on_button_click():
    val = ctypes.c_double(float(val_entry.get()))
    result = lib.convert_SI(val, l.unit_in, l.unit_out)
    result_var.set(result)


button = tk.Button(text="Convert", command=on_button_click)
button.grid(column=1, row=1)

result_var = tk.StringVar()
result_entry = tk.Entry(textvariable=result_var, state="readonly")
result_entry.grid(column=1, row=2)
