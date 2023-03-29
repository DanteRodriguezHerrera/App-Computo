import tkinter as tk
from functools import partial
from config.interfaz_config import callback,check_window_open,handle_focus_in,font_1,color_3
import config.interfaz_config as interfaz_config
import datetime
from tkinter import messagebox
from operaciones import add_loan,delete_loan,update_loan


def add_loan_window(ventana):

    check_window_open()
    
    #print(interfaz_config.counter_windows)
    if interfaz_config.counter_windows == 0:
        interfaz_config.counter_windows += 1
        new_loan_window = tk.Toplevel(ventana)
        new_loan_window.protocol("WM_DELETE_WINDOW", partial(callback,new_loan_window))
        new_loan_window.minsize(300,500)
        new_loan_window.title("Añadir préstamo")

        
        
        loanID_entry = tk.Entry(new_loan_window, font=('Helvetica 12'), fg="grey" )
        loanID_label = tk.Label(new_loan_window, text="ID del préstamo nuevo:")
        loanID_label.pack()

        loanID_entry.insert(tk.END, "Ejemplo: L-17")
        loanID_entry.pack(pady=5)

        loanID_entry.bind("<FocusIn>", handle_focus_in)
        




        loan_branchID_label = tk.Label(new_loan_window, text="ID de la sucursal del préstamo nuevo:")
        loan_branchID_label.pack()
        loan_branchID_entry = tk.Entry(new_loan_window, font=('Helvetica 12'), fg="grey")
        loan_branchID_entry.insert(tk.END, "Ejemplo: S0001")
        loan_branchID_entry.pack(pady=5)

        loan_branchID_entry.bind("<FocusIn>", handle_focus_in)



        loan_cantidad_label = tk.Label(new_loan_window, text="Cantidad del préstamo nuevo:")
        loan_cantidad_label.pack()
        loan_cantidad_entry = tk.Entry(new_loan_window, font=('Helvetica 12'), fg="grey")
        loan_cantidad_entry.insert(tk.END, "Ejemplo: 1800")
        loan_cantidad_entry.pack(pady=5)

        loan_cantidad_entry.bind("<FocusIn>", handle_focus_in)
        
        


        def ok():
            try:
                loanID = str(loanID_entry.get())
                loan_branchID = str(loan_branchID_entry.get())
                loan_cantidad = str(loan_cantidad_entry.get())

                print(f"add_branch({loanID}, {loan_branchID}, {loan_cantidad})")
                add_loan(loanID, loan_branchID, loan_cantidad)

            except Exception as e:
                messagebox.showerror("Error", e)


        boton = tk.Button(new_loan_window, text="Añadir préstamo", command=ok )

        boton.pack()

def delete_loan_window(ventana):

    check_window_open()
    

    if interfaz_config.counter_windows == 0:
        interfaz_config.counter_windows += 1
        delete_loan_window = tk.Toplevel(ventana)
        delete_loan_window.protocol("WM_DELETE_WINDOW", partial(callback, delete_loan_window))
        delete_loan_window.minsize(300,500)
        delete_loan_window.title("Eliminar sucursal")

        
        
        loanID_entry = tk.Entry(delete_loan_window, font=('Helvetica 12'), fg="grey" )
        loanID_label = tk.Label(delete_loan_window, text="ID del préstamo a eliminar:")
        loanID_label.pack()

        loanID_entry.insert(tk.END, "Ejemplo: L-17")
        loanID_entry.pack(pady=5)

        loanID_entry.bind("<FocusIn>", handle_focus_in)
        


        def ok():
            try:
                loanID = str(loanID_entry.get())

                print("delete_loan(",loanID,")")
                delete_loan(loanID)

            except Exception as e:
                messagebox.showerror("Error", e)
            

        boton = tk.Button(delete_loan_window, text="Eliminar préstamo", command=ok )

        boton.pack()


def update_loan_window(ventana):

    check_window_open()
    

    if interfaz_config.counter_windows == 0:
        interfaz_config.counter_windows += 1
        mod_loan_window = tk.Toplevel(ventana)
        mod_loan_window.protocol("WM_DELETE_WINDOW", partial(callback,mod_loan_window))
        mod_loan_window.minsize(300,500)
        mod_loan_window.title("Modificar préstamo")

        
        
        loanID_entry = tk.Entry(mod_loan_window, font=('Helvetica 12'), fg="grey" )
        loanID_label = tk.Label(mod_loan_window, text="ID del préstamo a modificar:")
        loanID_label.pack()

        loanID_entry.insert(tk.END, "Ejemplo: L-17")
        loanID_entry.pack(pady=5)

        loanID_entry.bind("<FocusIn>", handle_focus_in)
        




        loan_branchID_label = tk.Label(mod_loan_window, text="ID de la sucursal del préstamo a modificar:")
        loan_branchID_label.pack()
        loan_branchID_entry = tk.Entry(mod_loan_window, font=('Helvetica 12'), fg="grey")
        loan_branchID_entry.insert(tk.END, "Ejemplo: S0001")
        loan_branchID_entry.pack(pady=5)

        loan_branchID_entry.bind("<FocusIn>", handle_focus_in)



        loan_cantidad_label = tk.Label(mod_loan_window, text="Cantidad del préstamo a modificar:")
        loan_cantidad_label.pack()
        loan_cantidad_entry = tk.Entry(mod_loan_window, font=('Helvetica 12'), fg="grey")
        loan_cantidad_entry.insert(tk.END, "Ejemplo: 1800")
        loan_cantidad_entry.pack(pady=5)

        loan_cantidad_entry.bind("<FocusIn>", handle_focus_in)
        
        


        def ok():
            try:
                loanID = str(loanID_entry.get())
                loan_branchID = str(loan_branchID_entry.get())
                loan_cantidad = str(loan_cantidad_entry.get())

                print(f"update_loan({loanID}, {loan_branchID}, {loan_cantidad})")
                update_loan(loanID, loan_branchID, loan_cantidad)
            except Exception as e:
                messagebox.showerror("Error", e)

        boton = tk.Button(mod_loan_window, text="Actualizar sucursal", command=ok )

        boton.pack()



def show_all_loans_window(ventana):

    check_window_open()
    
    # Crear una lista de opciones
    #

    # Create the default window
    root = tk.Tk()
    root.title("Welcome to GeeksForGeeks")
    root.geometry('700x500')

    # Create the list of options
    opciones = ["Downtown", "Redwood", "Perryridge", "Mianus", "Round Hill", "Pownal", "North Town", "Brighton", "Central"]

    # Variable to keep track of the option
    # selected in OptionMenu
    value_inside = tk.StringVar(root)

    value_inside.set("Select an Option")

    question_menu = tk.OptionMenu(root, value_inside, *opciones)
    question_menu.pack()

    def print_answers():
        print("Selected Option: {}".format(value_inside.get()))
        return None

    # Crea un buton para confirmar la opcion seleccionada
    submit_button = tk.Button(root, text='Submit', command=print_answers)
    submit_button.pack()

    root.mainloop()



def create_branch_window(window):
    color_b = "gray92"
    branches = tk.Toplevel(window)
    branches.title("Sucursales")
    branches.minsize(300,300)
    tk.Label(branches, text="Sucursales").pack()

    add_branch_bt = tk.Button(branches, text='Añadir sucursal', font=(font_1, 12), bd=2, command=partial(add_loan_window, window) , cursor="hand2", bg=color_b,fg=color_3,width=25).pack(padx=5, pady=10)

    update_branch_bt = tk.Button(branches, text='Modificar sucursal', font=(font_1, 12), bd=2, command=partial(update_loan_window, window) , cursor="hand2", bg=color_b,fg=color_3,width=25).pack(padx=5, pady=10)

    delete_branch_bt = tk.Button(branches, text='Borrar sucursal', font=(font_1, 12), bd=2, command=partial(delete_loan_window, window) , cursor="hand2", bg=color_b,fg=color_3,width=25).pack(padx=5, pady=10)


    buscar_dept = tk.Button(branches, text='Mostrar sucursales', font=(font_1, 12), bd=2, command=partial(show_all_loans_window, window) , cursor="hand2", bg=color_b,fg=color_3,anchor=tk.CENTER,width=25).pack(padx=5, pady=10)

    
    