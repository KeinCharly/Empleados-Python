import mysql.connector

conexion = mysql.connector.connect(
    host = "charlydb.cb4cow8oeq2r.us-west-1.rds.amazonaws.com",
    user = "ChAdmin",
    password="K31n3ng3l#",
    database="EMPLEADOS"
)

cursor = conexion.cursor()

departamentos_por_puesto = {
    "QA Testes": "TI",
    "Analista QA": "TI",
    "IT": "TI",
    "People": "RH",
    "Marketing": "Sales",
    "Finanzas": "Administración",
    "Dir. Excecutive": "Dirección"
}

cursor.execute("SELECT id, puesto FROM empleados")
empleados = cursor.fetchall()

for emp_id, puesto in empleados:
    depto = departamentos_por_puesto.get(puesto, "Administración")
    cursor.execute("UPDATE empleados SET departamento = %s WHERE id = %s", (depto, emp_id))

conexion.commit()
print("Departamentos actualizados para todos los empleados.")

cursor.close()
conexion.close()
