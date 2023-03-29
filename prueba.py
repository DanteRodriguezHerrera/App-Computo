
import cx_Oracle
import time

connectionString = "banco/secret@localhost:4300/xe"
user='banco'
password='secret'
pool_size = 3

def conexion():
    start = time.time()
    try:
        dsn_tns = cx_Oracle.makedsn('localhost', '4300', service_name='xe') # reemplaza 'localhost' por el nombre o IP de tu servidor de Oracle
        #dbconn = cx_Oracle.connect(user='banco', password='secret', dsn=dsn_tns) # reemplaza 'usuario' y 'contraseña' con tus credenciales de Oracle
        pool = cx_Oracle.SessionPool(user=user, password=password, dsn=dsn_tns, min=pool_size, max=pool_size, increment=0)

        print("Conexión exitosa a Oracle")
        print("Tiempo de conexión: ", time.time() - start)
        return pool
    except cx_Oracle.Error as err:
        print(err)
        #messagebox.showerror(message="No se pudo establecer la conexión con la base de datos",title="Error")
        #window.destroy()

pool = conexion()

num_loan = 'pbpy'
branchID = 'S01'
quantity = 1000

try:
    # Crea un cursor y llama al procedimiento almacenado
    start_time1 = time.time()
    start_time = time.time()
    conn = pool.acquire()
    print("Tiempo de adquirir conexión: ", time.time() - start_time)
    start_time = time.time()
    cursor = conn.cursor()
    print("Tiempo de crear cursor: ", time.time() - start_time)
    start_time = time.time()
    cursor.callproc("insertar_prestamo", [num_loan, branchID, quantity])
    #cursor.callproc("eliminar_prestamo", [num_loan])
    print("Tiempo de ejecutar procedimiento: ", time.time() - start_time)
    start_time = time.time()
    conn.commit()
    print("Tiempo de hacer commit: ", time.time() - start_time)
    start_time = time.time()
    cursor.close()
    print("Tiempo de cerrar cursor: ", time.time() - start_time)
    start_time = time.time()
    pool.release(conn)
    print("Tiempo de liberar conexión: ", time.time() - start_time)
    #messagebox.showinfo(message=f'Sucursal creada con exito. Id de la sucursal:{branchID}')
    print(f'Prestamo creada con exito. No. del prestamo:{num_loan}')
    print("Tiempo de total ejecución: ", time.time() - start_time1)
except cx_Oracle.Error as error:
    #messagebox.showerror(message=error, title="Error")
    print(error)