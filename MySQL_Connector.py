import mysql.connector

conexion = mysql.connector.connect(
    host="charlydb.cb4cow8oeq2r.us-west-1.rds.amazonaws.com",
    user="ChAdmin",
    password="K31n3ng3l#",
    database="EMPLEADOS"
)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM empleados")

for fila in cursor.fetchall():
    print(fila)

cursor.close()
conexion.close()