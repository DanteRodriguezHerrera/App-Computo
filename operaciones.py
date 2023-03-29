from tkinter import messagebox
from datetime import datetime
import calendar
import pprint as pp
import tkinter as tk
from tkinter import ttk
import cx_Oracle

connectionString = "banco/secret@localhost:4300/xe"
user='banco'
password='secret'
pool_size = 3

#window
def conexion(window):
    try:
        dsn_tns = cx_Oracle.makedsn('localhost', '4300', service_name='xe') # reemplaza 'localhost' por el nombre o IP de tu servidor de Oracle
        #dbconn = cx_Oracle.connect(user='banco', password='secret', dsn=dsn_tns) # reemplaza 'usuario' y 'contraseña' con tus credenciales de Oracle
        pool = cx_Oracle.SessionPool(user=user, password=password, dsn=dsn_tns, min=pool_size, max=pool_size, increment=0)

        print("Conexión exitosa a Oracle")
        return pool
    except cx_Oracle.Error as err:
        print(err)
        messagebox.showerror(message="No se pudo establecer la conexión con la base de datos",title="Error")
        window.destroy()

def add_branch(branchID, branch_name, branch_city, branch_active, branch_region):
    """Añade una sucursal

    Parameters
    ----------
        branchID: Numero de la sucursal.
        branch_name: Nombre de la sucursal.
        branch_city: Ciudad de la sucursal.
        branch_active: Activo de la sucursal.
        branch_region: Region de la sucursal.

    Return
    ------
    None
    """

    try:
        # Crea un cursor y llama al procedimiento almacenado
        with cx_Oracle.connect(connectionString) as conn:
            with conn.cursor() as cursor:

                cursor.callproc("insertar_sucursal", [branchID, branch_name, branch_city, branch_active, branch_region])
                conn.commit()

        messagebox.showinfo(message=f'Sucursal creada con exito. Id de la sucursal:{branchID}')
        print(f'Sucursal creada con exito. Id de la sucursal:{branchID}')
    except cx_Oracle.Error as error:
        messagebox.showerror(message=error, title="Error")
        print(error)

def update_branch(branchID, branch_name, branch_city, branch_active, branch_region):
    """Modifica una sucursal

    Parameters
    ----------
        branchID: Numero de la sucursal.
        branch_name: Nombre de la sucursal.
        branch_city: Ciudad de la sucursal.
        branch_active: Activo de la sucursal.
        branch_region: Region de la sucursal.

    Return
    ------
    None
    """

    try:
        # Crea un cursor y llama al procedimiento almacenado
        with cx_Oracle.connect(connectionString) as conn:
            with conn.cursor() as cursor:

                cursor.callproc("modificar_sucursal", [branchID, branch_name, branch_city, branch_active, branch_region])
                conn.commit()

        messagebox.showinfo(message=f'Sucursal modificada con exito. Id de la sucursal:{branchID}')
        print(f'Sucursal modificada con exito. Id de la sucursal:{branchID}')
    except cx_Oracle.Error as error:
        messagebox.showerror(message=error, title="Error")
        print(error)

def delete_branch(branchID):
    """Elimina una sucursal

    Parameters
    ----------
        branchID: Numero de la sucursal.

    Return
    ------
    None
    """

    try:
        # Crea un cursor y llama al procedimiento almacenado
        with cx_Oracle.connect(connectionString) as conn:
            with conn.cursor() as cursor:

                cursor.callproc("eliminar_sucursal", [branchID])
                conn.commit()

        messagebox.showinfo(message=f'Sucursal borrada con exito. Id de la sucursal:{branchID}')
        print(f'Sucursal eliminada con exito. Id de la sucursal:{branchID}')
    except cx_Oracle.Error as error:
        messagebox.showerror(message=error, title="Error")
        print(error)


def add_loan(num_loan, branchID, quantity):
    """Añade una sucursal

    Parameters
    ----------
        branchID: Numero de la sucursal.
        branch_name: Nombre de la sucursal.
        branch_city: Ciudad de la sucursal.
        branch_active: Activo de la sucursal.
        branch_region: Region de la sucursal.

    Return
    ------
    None
    """

    try:
        # Crea un cursor y llama al procedimiento almacenado
        with cx_Oracle.connect(connectionString) as conn:
            with conn.cursor() as cursor:

                cursor.callproc("insertar_prestamo", [num_loan, branchID, quantity])
                conn.commit()

        messagebox.showinfo(message=f'Prestamo creado con exito. Id de la sucursal:{num_loan}')
        print(f'Prestamo creado con exito. No. del prestamo:{num_loan}')
    except cx_Oracle.Error as error:
        messagebox.showerror(message=error, title="Error")
        print(error)

def update_loan(num_loan, branchID, quantity):
    """Añade una sucursal

    Parameters
    ----------
        noprestamo: Numero de la sucursal.
        idsucursal: Nombre de la sucursal.
        cantididad: Activo de la sucursal.

    Return
    ------
    None
    """

    try:
        # Crea un cursor y llama al procedimiento almacenado
        with cx_Oracle.connect(connectionString) as conn:
            with conn.cursor() as cursor:

                cursor.callproc("modificar_prestamo", [num_loan, branchID, quantity])
                conn.commit()

        messagebox.showinfo(message=f'Prestamo acutalizado con exito. ID:{num_loan}')
        print(f'Prestamo actualizado con exito. No. del prestamo:{num_loan}')
    except cx_Oracle.Error as error:
        messagebox.showerror(message=error, title="Error")
        print(error)

def delete_loan(num_loan):
    """Elimina una sucursal

    Parameters
    ----------
        noprestamo: Numero de la sucursal.

    Return
    ------
    None
    """

    try:
        # Crea un cursor y llama al procedimiento almacenado
        with cx_Oracle.connect(connectionString) as conn:
            with conn.cursor() as cursor:

                cursor.callproc("eliminar_prestamo", [num_loan])
                conn.commit()

        messagebox.showinfo(message=f'Prestamo borrado con exito. ID:{num_loan}')
        print(f'Prestamo eliminado con exito. No. del prestamo:{num_loan}')
    except cx_Oracle.Error as error:
        messagebox.showerror(message=error, title="Error")
        print(error)

def show_all_branches():
    """Muestra todas las sucursales

    Parameters
    ----------

    Return
    ------
    None
    """

    try:
        # Crea un cursor y llama al procedimiento almacenado
        with cx_Oracle.connect(connectionString) as conn:
            with conn.cursor() as cursor:

                # Ejecutar la consulta
                cursor.callproc("DBMS_MVIEW.REFRESH", ['mv_sucursal_global'])
                cursor.execute("SELECT * FROM mv_sucursal_global")
                conn.commit()
                # Recorrer el cursor e imprimir los resultados

                # Crear una ventana de tkinter
                window = tk.Tk()
                window.title("Sucursales")

                # Crear una tabla en tkinter
                table = ttk.Treeview(window)

                # Configurar las columnas de la tabla
                table["columns"] = [column[0] for column in cursor.description]
                table.column("#0", width=50, minwidth=50)
                for column in cursor.description:
                    print(column[0])
                    table.column(column[0],  anchor="w")
                    table.heading(column[0], text=column[0])

                # Encabezados de las columnas
                table.heading("#0", text="ID", anchor=tk.CENTER)

                # Agregar los datos de la tabla a la tabla en tkinter
                i=1
                for row in cursor:
                    table.insert(parent="", index = tk.END,text=f"{i}" , iid=i, values=row)
                    i+=1

                # Mostrar la tabla en la ventana de tkinter
                table.pack()
                
                

    except cx_Oracle.Error as error:
        messagebox.showerror(message=error, title="Error")
        print(error)

def show_all_loans():
    """Muestra todos los prestamos

    Parameters
    ----------

    Return
    ------
    None
    """

    try:
        # Crea un cursor y llama al procedimiento almacenado
        with cx_Oracle.connect(connectionString) as conn:
            with conn.cursor() as cursor:

                # Ejecutar la consulta
                cursor.callproc("DBMS_MVIEW.REFRESH", ['mv_prestamo_global'])
                cursor.execute("SELECT * FROM mv_prestamo_global")
                conn.commit()
                # Recorrer el cursor e imprimir los resultados

                 # Crear una ventana de tkinter
                window = tk.Tk()
                window.title("Prestamos")

                # Crear una tabla en tkinter
                table = ttk.Treeview(window)

                # Configurar las columnas de la tabla
                table["columns"] = [column[0] for column in cursor.description]
                table.column("#0", width=50, minwidth=50)
                for column in cursor.description:
                    print(column[0])
                    table.column(column[0],  anchor="w")
                    table.heading(column[0], text=column[0])

                # Encabezados de las columnas
                table.heading("#0", text="ID", anchor=tk.CENTER)

                # Agregar los datos de la tabla a la tabla en tkinter
                i=1
                for row in cursor:
                    table.insert(parent="", index = tk.END,text=f"{i}" , iid=i, values=row)
                    i+=1

                # Mostrar la tabla en la ventana de tkinter
                table.pack()

                

    except cx_Oracle.Error as error:
        messagebox.showerror(message=error, title="Error")
        print(error)

def show_all_loans_on_branch():
    """muestra todos los prestamos por sucursal
    Parameters
    ----------

    Return
    ------
    None
    """
    
    try:
        # Crea un cursor y llama al procedimiento almacenado
        with cx_Oracle.connect(connectionString) as conn:
            with conn.cursor() as cursor:
                # Ejecutar la consulta
                cursor.callproc("DBMS_MVIEW.REFRESH", ['mv_prestamos_por_sucursal'])
                cursor.execute("SELECT * FROM mv_prestamos_por_sucursal")
                conn.commit()
                # Recorrer el cursor e imprimir los resultados

                # Crear una ventana de tkinter
                window = tk.Tk()
                window.title("Prestamos por sucursal")
                # Crear una tabla en tkinter
                table = ttk.Treeview(window)

                # Configurar las columnas de la tabla
                table["columns"] = [column[0] for column in cursor.description]
                table.column("#0", width=50, minwidth=50)
                for column in cursor.description:
                    print(column[0])
                    table.column(column[0],  anchor="w")
                    table.heading(column[0], text=column[0])

                # Encabezados de las columnas
                table.heading("#0", text="ID", anchor=tk.CENTER)

                # Agregar los datos de la tabla a la tabla en tkinter
                i=1
                for row in cursor:
                    table.insert(parent="", index = tk.END,text=f"{i}" , iid=i, values=row)
                    i+=1

                # Mostrar la tabla en la ventana de tkinter
                table.pack()
                
                
                

    except cx_Oracle.Error as error:
        messagebox.showerror(message=error, title="Error")
        print(error)