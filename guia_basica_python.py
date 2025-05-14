
# 1. Mostrar algo en pantalla
print("Hola, Carlos")

# 2. Variables y tipos de datos
nombre = "Carlos"
edad = 30
es_activo = True

# 3. Condicionales
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# 4. Bucles
# For
for i in range(5):
    print(i)  # Imprime del 0 al 4

# While
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# 5. Funciones
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Carlos")

# 6. Listas
frutas = ["manzana", "banana", "naranja"]
print(frutas[0])  # manzana

# 7. Diccionarios
persona = {"nombre": "Carlos", "edad": 30}
print(persona["nombre"])

# 8. Manejo de errores
try:
    division = 10 / 0
except ZeroDivisionError:
    print("No puedes dividir entre cero")

# 9. Importar módulos
import math
print(math.sqrt(16))  # Raíz cuadrada de 16

# 10. Comentarios
# Esto es un comentario de una línea
"""
Esto es un
comentario de varias líneas
"""
