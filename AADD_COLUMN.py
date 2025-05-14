import mysql.connector

conexion = mysql.connector.connect(
    host = "charlydb.cb4cow8oeq2r.us-west-1.rds.amazonaws.com",
    user = "ChAdmin",
    password="K31n3ng3l#",
    database="EMPLEADOS"
)

cursor = conexion.cursor()

cursor.execute("ALTER TABLE empleados ADD COLUMN departamento VARCHAR(50)")
conexion.commit()

print("Columna 'departamento' agregada exitosamente.")

cursor.close()
conexion.close()
