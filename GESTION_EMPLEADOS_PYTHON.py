# Sitema de Gestión de Empleados

empleados = []

# Función para agregar empleado

def agregar_empleado():
    id_empleado = input("ID del empleado: ")
    nombre = input("Nombre: ")
    puesto = input("Puesto: ")
    salario = input("Salario: ")
    empleado = {
        "id": id_empleado,
        "nombre": nombre,
        "puesto": puesto,
        "salario": salario
    }
    empleados.append(empleado)
    print("Empleado agregado correctamente.\n")

#Función para listar empleados
def listar_empleados():
    if not empleados:
        print("No hay empleados regitrados\n")
        return
    for emp in empleados:
        print(f"ID: {emp['id']}, Nombre: {emp['nombre']}, Puesto: {emp['puesto']}, Salario: {emp['salario']}")
    print()

# Función para buscar por ID
def buscar_empleado():
    id_buscar = input("Ingresa el ID del empleado: ")
    for emp in empleados:
        if emp['id'] == id_buscar:
            print(f"Encontrado: {emp}\n")
            return
    print("Empleado no encontrado. \n")        

#Función para actualizar empleado
def actualizar_empleado():
    id_actualizar = input("ID del empleado a actualizar: ")
    for emp in empleados:
        if emp['id'] == id_actualizar:
            emp['nombre'] == input("Nuevo nombre: ")
            emp['puesto'] == input("Nuevo puesto: ")
            emp['salario'] == input("Nuevo salario: ")
            print("Empleado actualizado. \n")
            return
    print("Empleado no encontrado. \n")    

#Función para elimninar empleado
def eliminar_empleado():
    id_eliminar = input("ID del empleado a eliminar: ")
    for i, emp in enumerate(empleados):
        if emp['id'] == id_eliminar:
            del empleados[i]
            print("Empleado eliminado. \n")
            return
        print("Empleado no encontrado. \n")

# Menpu principal
def menu():
    while True:
        print("\n--- Sistema de Gestión de Empleados ---")
        print("1. Agregar empleado")
        print("2. Listar empleados")
        print("3. Buscar empleado por ID")
        print("4. Actualizar empleado")
        print("5. Eliminar Empleado")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            agregar_empleado()
        elif opcion == "2":
            listar_empleados()
        elif opcion == "3":
            buscar_empleado()
        elif opcion == "4":
            actualizar_empleado()
        elif opcion == "5":
            eliminar_empleado()
        elif opcion == "6":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opcion inválida. Intenta nuevamente. \n")

#Ejecutar el menú
if __name__ == "__main__":
    menu()

