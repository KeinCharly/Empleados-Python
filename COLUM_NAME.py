import mysql.connector

conexion = mysql.connector.connect(
    host = "charlydb.cb4cow8oeq2r.us-west-1.rds.amazonaws.com",
    user = "ChAdmin",
    password="K31n3ng3l#",
    database="EMPLEADOS"
)
cursor = conexion.cursor()
cursor.execute("DESCRIBE empleados")

for columna in cursor.fetchall():
    print(columna)

cursor.close()
conexion.close()
