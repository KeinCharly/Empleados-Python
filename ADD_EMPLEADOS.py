import mysql.connector

conexion = mysql.connector.connect(
    host = "charlydb.cb4cow8oeq2r.us-west-1.rds.amazonaws.com",
    user = "ChAdmin",
    password = "K31n3ng3l#",
    database = "EMPLEADOS"
)

cursor = conexion.cursor()

sql = "INSERT INTO empleados (nombre, puesto, salario) VALUES (%s, %s, %s)"
valores = ("Laura Garcia", "Analista QA", 20000)

cursor.execute(sql, valores)
conexion.commit()

print (f"Empleado intertado. ID {cursor.lastrowid}")

cursor.close()
conexion.close()
