import tkinter as tk
from functools import partial
from config.interfaz_config import callback,check_window_open,handle_focus_in,font_1,color_3
import config.interfaz_config as interfaz_config
from tkinter import messagebox
from operaciones import add_branch,update_branch,delete_branch, show_all_branches

# from interfaces.branches import add_branch_window, update_branch_window, delete_branch_window, show_all_branches_window
def add_branch_window(ventana):

    check_window_open()
    
    #print(interfaz_config.counter_windows)
    if interfaz_config.counter_windows == 0:
        interfaz_config.counter_windows += 1
        new_branch_window = tk.Toplevel(ventana)
        new_branch_window.protocol("WM_DELETE_WINDOW", partial(callback,new_branch_window))
        new_branch_window.minsize(300,500)
        new_branch_window.title("Añadir sucursal")

        
        
        branchID_entry = tk.Entry(new_branch_window, font=('Helvetica 12'), fg="grey" )
        branchID_label = tk.Label(new_branch_window, text="ID de la sucursal nueva:")
        branchID_label.pack()

        branchID_entry.insert(tk.END, "Ejemplo: S0321")
        branchID_entry.pack(pady=5)

        branchID_entry.bind("<FocusIn>", handle_focus_in)
        


        branch_nombre_label = tk.Label(new_branch_window, text="Nombre de la sucursal nueva:")
        branch_nombre_label.pack()
        branch_nombre_entry = tk.Entry(new_branch_window, font=('Helvetica 12'), fg="grey")
        branch_nombre_entry.insert(tk.END, "Ejemplo: Downtown")
        branch_nombre_entry.pack(pady=5)

        branch_nombre_entry.bind("<FocusIn>", handle_focus_in)
        


        branch_city_label = tk.Label(new_branch_window, text="Ciudad de la sucursal nueva:")
        branch_city_label.pack()
        branch_city_entry = tk.Entry(new_branch_window, font=('Helvetica 12'), fg="grey")
        branch_city_entry.insert(tk.END, "Ejemplo: Brooklyn")
        branch_city_entry.pack(pady=5)

        branch_city_entry.bind("<FocusIn>", handle_focus_in)



        branch_active_label = tk.Label(new_branch_window, text="Activos de la sucursal nueva:")
        branch_active_label.pack()
        branch_active_entry = tk.Entry(new_branch_window, font=('Helvetica 12'), fg="grey")
        branch_active_entry.insert(tk.END, "Ejemplo: 900000")
        branch_active_entry.pack(pady=5)

        branch_active_entry.bind("<FocusIn>", handle_focus_in)



        branch_region_label = tk.Label(new_branch_window, text="Region de la sucursal nueva:")
        branch_region_label.pack()
        branch_region_entry = tk.Entry(new_branch_window, font=('Helvetica 12'), fg="grey")
        branch_region_entry.insert(tk.END, "Ejemplo: 1")
        branch_region_entry.pack(pady=5)

        branch_region_entry.bind("<FocusIn>", handle_focus_in)
        
        def ok():
            try:
                branchID = str(branchID_entry.get())
                branch_name = str(branch_nombre_entry.get())
                branch_city = str(branch_city_entry.get())
                branch_active = int(branch_active_entry.get())
                branch_region = int(branch_region_entry.get())
                print("branchID en compras",branchID)
                branch = add_branch(branchID, branch_name, branch_city, branch_active, branch_region)

            except Exception as error:
                messagebox.showerror("Error", error)
                return

            print(f"add_branch({branchID}, {branch_name}, {branch_city}, {branch_active}, {branch_region})")

        boton = tk.Button(new_branch_window, text="Añadir sucursal", command=ok )

        boton.pack()

def delete_branch_window(ventana):

    check_window_open()
    

    if interfaz_config.counter_windows == 0:
        interfaz_config.counter_windows += 1
        delete_branch_window = tk.Toplevel(ventana)
        delete_branch_window.protocol("WM_DELETE_WINDOW", partial(callback, delete_branch_window))
        delete_branch_window.minsize(300,500)
        delete_branch_window.title("Eliminar sucursal")

        
        branchID_entry = tk.Entry(delete_branch_window, font=('Helvetica 12'), fg="grey" )
        branchID_label = tk.Label(delete_branch_window, text="ID de la sucursal a eliminar:")
        branchID_label.pack()

        branchID_entry.insert(tk.END, "Ejemplo: S0321")
        branchID_entry.pack(pady=5)

        branchID_entry.bind("<FocusIn>", handle_focus_in)
        

        def ok():
            try:
                branchID = str(branchID_entry.get())

                print("delete_depto(",branchID,")")
                delete_branch(branchID)
            except Exception as error:
                messagebox.showerror("Error", error)
                return
            

        boton = tk.Button(delete_branch_window, text="Eliminar sucursal", command=ok )

        boton.pack()


def update_branch_window(ventana):

    check_window_open()
    
    if interfaz_config.counter_windows == 0:
        interfaz_config.counter_windows += 1
        mod_branch_window = tk.Toplevel(ventana)
        mod_branch_window.protocol("WM_DELETE_WINDOW", partial(callback,mod_branch_window))
        mod_branch_window.minsize(300,500)
        mod_branch_window.title("Modificar sucursal")

        
        branchID_entry = tk.Entry(mod_branch_window, font=('Helvetica 12'), fg="grey" )
        branchID_label = tk.Label(mod_branch_window, text="ID de la sucursal a modificar:")
        branchID_label.pack()

        branchID_entry.insert(tk.END, "Ejemplo: S0321")
        branchID_entry.pack(pady=5)

        branchID_entry.bind("<FocusIn>", handle_focus_in)
        

        branch_nombre_label = tk.Label(mod_branch_window, text="Nombre de la sucursal a modificar:")
        branch_nombre_label.pack()
        branch_nombre_entry = tk.Entry(mod_branch_window, font=('Helvetica 12'), fg="grey")
        branch_nombre_entry.insert(tk.END, "Ejemplo: Downtown")
        branch_nombre_entry.pack(pady=5)

        branch_nombre_entry.bind("<FocusIn>", handle_focus_in)
        

        branch_city_label = tk.Label(mod_branch_window, text="Ciudad de la sucursal a modificar:")
        branch_city_label.pack()
        branch_city_entry = tk.Entry(mod_branch_window, font=('Helvetica 12'), fg="grey")
        branch_city_entry.insert(tk.END, "Ejemplo: Brooklyn")
        branch_city_entry.pack(pady=5)

        branch_city_entry.bind("<FocusIn>", handle_focus_in)


        branch_active_label = tk.Label(mod_branch_window, text="Activos de la sucursal a modificar:")
        branch_active_label.pack()
        branch_active_entry = tk.Entry(mod_branch_window, font=('Helvetica 12'), fg="grey")
        branch_active_entry.insert(tk.END, "Ejemplo: 900000")
        branch_active_entry.pack(pady=5)

        branch_active_entry.bind("<FocusIn>", handle_focus_in)


        branch_region_label = tk.Label(mod_branch_window, text="Region de la sucursal a modificar:")
        branch_region_label.pack()
        branch_region_entry = tk.Entry(mod_branch_window, font=('Helvetica 12'), fg="grey")
        branch_region_entry.insert(tk.END, "Ejemplo: 1")
        branch_region_entry.pack(pady=5)

        branch_region_entry.bind("<FocusIn>", handle_focus_in)

        def ok():
            try:
                branchID = str(branchID_entry.get())
                branch_name = str(branch_nombre_entry.get())
                branch_city = str(branch_city_entry.get())
                branch_active = int(branch_active_entry.get())
                branch_region = int(branch_region_entry.get())
                
                print(f"update_branch({branchID}, {branch_name}, {branch_city}, {branch_active}, {branch_region})")
                branch = update_branch(branchID, branch_name, branch_city, branch_active, branch_region)
            except Exception as error:
                messagebox.showerror("Error", error)
                return

        boton = tk.Button(mod_branch_window, text="Actualizar sucursal", command=ok )

        boton.pack()



def show_all_branches_window(ventana):

    check_window_open()
    

    if interfaz_config.counter_windows == 0:
        interfaz_config.counter_windows += 1
        empleados_windows = tk.Toplevel(ventana)
        empleados_windows.protocol("WM_DELETE_WINDOW", partial(callback,empleados_windows))
        empleados_windows.minsize(300,500)
        empleados_windows.title("Mostrar sucursales")


        boton = tk.Button(empleados_windows, text="Mostrar sucursales", command=show_all_branches)

        boton.pack()


def create_branch_window(window):
    color_b = "gray92"
    branches = tk.Toplevel(window)
    branches.title("Sucursales")
    branches.minsize(300,300)
    tk.Label(branches, text="Sucursales").pack()

    add_branch_bt = tk.Button(branches, text='Añadir sucursal', font=(font_1, 12), bd=2, command=partial(add_branch_window, window) , cursor="hand2", bg=color_b,fg=color_3,width=25).pack(padx=5, pady=10)

    update_branch_bt = tk.Button(branches, text='Modificar sucursal', font=(font_1, 12), bd=2, command=partial(update_branch_window, window) , cursor="hand2", bg=color_b,fg=color_3,width=25).pack(padx=5, pady=10)

    delete_branch_bt = tk.Button(branches, text='Borrar sucursal', font=(font_1, 12), bd=2, command=partial(delete_branch_window, window) , cursor="hand2", bg=color_b,fg=color_3,width=25).pack(padx=5, pady=10)

    buscar_dept = tk.Button(branches, text='Mostrar sucursales', font=(font_1, 12), bd=2, command=partial(show_all_branches_window, window) , cursor="hand2", bg=color_b,fg=color_3,anchor=tk.CENTER,width=25).pack(padx=5, pady=10)

    