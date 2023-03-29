import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Crear el Treeview
tree = ttk.Treeview(root)

# Agregar columnas
tree["columns"] = ("one", "two", "three")
tree.column("#0", width=70, minwidth=70)
tree.column("one", width=150, minwidth=150)
tree.column("two", width=400, minwidth=200)
tree.column("three", width=80, minwidth=50)

# Encabezados de las columnas
tree.heading("#0", text="ID", anchor=tk.CENTER)
tree.heading("one", text="Nombre", anchor=tk.CENTER)
tree.heading("two", text="Descripción", anchor=tk.CENTER)
tree.heading("three", text="Cantidad", anchor=tk.CENTER)

# Agregar filas con un bucle for
for i in range(10):
    tree.insert(parent="", index=i, iid=i, text=f"{i+1}", values=(f"Item {i+1}", f"Descripción del Item {i+1}", f"{i+1}"))

tree.pack()
root.mainloop()
