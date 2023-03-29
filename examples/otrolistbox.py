import tkinter as tk
 
window = tk.Tk()
window.title('My Window')
 
window.geometry('500x300')
 
var1 = tk.StringVar()
l = tk.Label(window, bg='green', fg='yellow',font=('Arial', 12), width=10, textvariable=var1)
l.pack()
 
def print_selection():
    value = lb.get(lb.curselection())   
    var1.set(value)
 

 
var2 = tk.StringVar()
var2.set((1,2,3,4))
lb = tk.Listbox(window, listvariable=var2)

list_items = [11,22,33,44,55,66,77,88,99]
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'first')
lb.insert(2, 'second')
lb.delete(2)
lb.pack()



scrollbar = tk.Scrollbar(window)
scrollbar.pack(side = tk.RIGHT, fill = tk.BOTH)

lb.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lb.yview)
# Adding Scrollbar to the right
# side of root window

boton_agregar_producto = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
boton_agregar_producto.pack()
 
window.mainloop()