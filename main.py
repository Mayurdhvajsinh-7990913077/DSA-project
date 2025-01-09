import tkinter as tk
from tkinter import messagebox

def show_as_list():
    elements = list_entry.get().split(',')
    if elements == ['']:
        messagebox.showerror("Error", "Please enter some elements.")
    else:
        messagebox.showinfo("List", str(elements))

def show_as_tuple():
    elements = tuple_entry.get().split(',')
    if elements == ['']:
        messagebox.showerror("Error", "Please enter some elements.")
    else:
        messagebox.showinfo("Tuple", str(tuple(elements)))

def show_as_set():
    elements = set_entry.get().split(',')
    if elements == ['']:
        messagebox.showerror("Error", "Please enter some elements.")
    else:
        parsed_elements = set()
        for e in elements:
            if e == '1' and 'True' in parsed_elements:
                continue
            if e == 'True' and '1' in parsed_elements:
                continue
            if e == '0' and 'False' in parsed_elements:
                continue
            if e == 'False' and '0' in parsed_elements:
                continue
            parsed_elements.add(e)
        messagebox.showinfo("Set", str(parsed_elements))

# Create the main window
root = tk.Tk()
root.title("Element Converter")

# Create and place the input fields
list_label = tk.Label(root, text="Enter elements for List separated by commas:")
list_label.pack()
list_entry = tk.Entry(root, width=50)
list_entry.pack()

tuple_label = tk.Label(root, text="Enter elements for Tuple separated by commas:")
tuple_label.pack()
tuple_entry = tk.Entry(root, width=50)
tuple_entry.pack()

set_label = tk.Label(root, text="Enter elements for Set separated by commas:")
set_label.pack()
set_entry = tk.Entry(root, width=50)
set_entry.pack()

# Create and place the buttons
list_button = tk.Button(root, text="List", command=show_as_list)
list_button.pack()

tuple_button = tk.Button(root, text="Tuple", command=show_as_tuple)
tuple_button.pack()

set_button = tk.Button(root, text="Set", command=show_as_set)
set_button.pack()

# Run the application
root.mainloop()
