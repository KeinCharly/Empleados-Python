import mysql.connector

conexion = mysql.connector.connect(
    host = "charlydb.cb4cow8oeq2r.us-west-1.rds.amazonaws.com",
    user = "ChAdmin",
    password="K31n3ng3l#",
    database="EMPLEADOS"
)

cursor = conexion.cursor()

print("Buscar empleado por:")
print("1. ID")
print("2. Nombre")
opcion = input("Elige una opción (1 ó 2):")

if opcion == "1":
    id_buscar = input("Ingresa el ID del Empleado: ")
    cursor.execute("SELECT * FROM empleados WHERE id = %s", (id_buscar,))
elif opcion == "2":
    nombre_buscar = input("Ingresa el nombre del empleado: ")
    cursor.execute("SELECT * FROM empleados WHERE nombre LIKE %s", (f"%{nombre_buscar}%",))
else:
    print("Opción no válida.")

resultados = cursor.fetchall()

if resultados:
    for fila in resultados:
        print(fila)
else:
    print("No se encontraron resultados.")

cursor.close()
conexion.close()