
# EJERCICIOS BÁSICOS DE PYTHON

# 1. Imprime tu nombre en pantalla
# Escribe aquí tu código:
nombre = "Hello, Charly"
print(nombre)


# 2. Crea una variable con tu edad y muestra si eres mayor de edad
# Escribe aquí tu código:

edad = 25
if edad >= 18:
	print("Eres mayor de edad.")
else:
	print("Eres menor de edad")

# 3. Recorre los números del 1 al 10 e imprime si son pares o impares
# Escribe aquí tu código:

for numero in range(1, 11):
	if numero % 2 == 0:
		print(f"{numero} es par")
	else:
		print(f"{numero} es impar")


# 4. Crea una función que reciba un nombre y salude a la persona
# Escribe aquí tu código:

nombre = input("Ingresa tu nombre:")
print("Hi, " +nombre+ "!")
CORRECTO:
def saludar(nombre):
	print(f"Hi, {nombre}!")

saludar("Charly")

# 5. Crea una lista con al menos 5 frutas y recorre cada una con un bucle
# Escribe aquí tu código:

frutas = ["Sandía", "Mango", "Piña", "Melón", "Kiwi"]
for fruta in frutas:
	print(fruta)
Métodos de listas
Las listas en Python tienen varios métodos incorporados que nos permiten
manipular y modificar los elementos de la lista. Algunos métodos comunes son:
append(elemento): agrega un elemento al final de la lista.
insert(indice, elemento): inserta un elemento en una posición específica de la lista.
remove(elemento): elimina la primera aparición de un elemento en la lista.
pop(indice): elimina y devuelve el elemento en una posición específica de la lista.
sort(): ordena los elementos de la lista en orden ascendente.
reverse(): invierte el orden de los elementos en la lista.
Ejemplo:
frutas = ["manzana", "banana", "naranja"]
frutas.append("pera")
print(frutas)  # Imprime ["manzana", "banana", "naranja", "pera"]
frutas.insert(1, "uva")
print(frutas)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]
frutas.remove("banana")
print(frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]
fruta_eliminada = frutas.pop(2)
print(frutas)  # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"
frutas.sort()
print(frutas)  # Imprime ["manzana", "pera", "uva"]
frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "manzana"]

Listas de comprensión
Las listas de comprensión son una forma concisa de crear nuevas listas
basadas en una secuencia existente. Permiten filtrar y transformar los elementos
de una lista en una sola línea de código.

nueva_lista = [expresion for elemento in secuencia if condicion]
Ejemplo:

numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)  # Imprime [4, 16]
En este ejemplo, se crea una nueva lista llamada cuadrados, que contiene
los cuadrados de los números pares de la lista numeros.
La expresión x ** 2 eleva cada elemento al cuadrado,
y la condición if x % 2 == 0 filtra solo los números pares.


# 6. Crea un diccionario con los datos de una persona (nombre, edad, ciudad) e imprime los valores
# Escribe aquí tu código:

persona = {"Nombre": "Jack Richmond", "Edad": 82, "Ciudad": "Amburgo"}
print(persona["Nombre"])
print(persona["Edad"])
print(persona["Ciudad"])

Métodos de diccionarios
Los diccionarios en Python tienen varios métodos incorporados para manipular y acceder a los elementos. Algunos métodos comunes son:

keys(): devuelve una vista de todas las claves del diccionario.
values(): devuelve una vista de todos los valores del diccionario.
items(): devuelve una vista de todos los pares clave-valor del diccionario.
update(otro_diccionario): actualiza el diccionario con los pares clave-valor de otro diccionario.
Ejemplo:
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

print(persona.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"])
print(persona.values())  # Imprime dict_values(["Juan", 25, "Madrid"])
print(persona.items())   # Imprime dict_items([("nombre", "Juan"), ("edad", 25), ("ciudad", "Madrid")])


persona.update({"profesion": "Ingeniero"})
print(persona)  # Imprime {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "profesion": "Ingeniero"}

# 7. Usa try-except para manejar una división entre cero
# Escribe aquí tu código:

try:
	resultado = 10/0
	print(resultado)
except ZeroDivisionError:
	print("Error:División por Cero")
except ValueError:
	print("Error: Valor inválido")

# 8. Escribe una función que reciba un número y devuelva su cuadrado
# Escribe aquí tu código:

resulado = sqrt(25)
print(resultado)
CORRECTO:
def cuadrado(numero):
	return numero ** 2

print(cuadrado(5))

# 9. Importa el módulo random y genera un número aleatorio entre 1 y 100
# Escribe aquí tu código:

import random

numero_aleatorio = random.randint(1, 100)
print(numero_aleatorio)

# 10. Usa un comentario de varias líneas para describir qué aprendiste hoy
# Escribe aquí tu código:

def aprendizaje_Python(aprendido, repasado):
"""
En estos ejercicios aprendí a utilizar Funciones, Duplas, Llamar Módulos,
Diccionarios, Listas, Funciones FOR, Imprimir textos sencillos como
el nombre y edad de una persona, la base de la programación en Python se
encuentra en estos ejercicios básicos, que me ha ayudado a introducirme 
en el mundo de la programación de Python.
"""
CORRECTO:
"""
En estos ejercicios aprendí a utilizar funciones, diccionarios, listas, módulos, bucles y condicionales.
Me ayudó a entender lo básico de la programación en Python.
"""

# 11. Funciones con número variable de argumentos
Python permite definir funciones que acepten un número variable de argumentos. 
Esto se logra utilizando el operador * antes del nombre del parámetro.

def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


print(suma_variable(1, 2, 3))  # Imprime 6
print(suma_variable(4, 5, 6, 7))  # Imprime 22

# 12. Entrada de datos del usuario
Para obtener información del usuario durante la ejecución del programa, podemos utilizar la función input().
Esta función muestra un mensaje en la pantalla y espera a que el usuario ingrese un valor.

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")


print("Hola, " + nombre + "!")
print("Tienes " + edad + " años.")

En este ejemplo, se solicita al usuario que ingrese su nombre y edad utilizando la función input().
Los valores ingresados se almacenan en las variables nombre y edad, respectivamente.
Luego, se utilizan estas variables para mostrar un saludo personalizado en la pantalla.

edad = int(input("Ingresa tu edad: "))


if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
En este ejemplo, se solicita al usuario que ingrese su edad y se convierte el valor ingresado a un número entero utilizando int().
Luego, se utiliza una estructura condicional para verificar si la edad es mayor o igual a 18 y mostrar un mensaje correspondiente.

# 13. Salida de datos
Para mostrar información en la pantalla, utilizamos la función print().
Esta función toma uno o más argumentos y los muestra en la consola.
Podemos utilizar la f-string (formateo de cadenas) para incrustar variables directamente dentro de una cadena de texto.

nombre = "Juan"
edad = 25


print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")

# 14. Estructuras condicionales

Las estructuras condicionales nos permiten ejecutar diferentes bloques de código según se cumpla o no una determinada condición.
En Python, las estructuras condicionales más utilizadas son if, if-else y if-elif-else.

IF

La estructura if se utiliza para ejecutar un bloque de código si una condición es verdadera.
La sintaxis básica es la siguiente:

if condicion:

   # Bloque de código a ejecutar si la condición es verdadera
   instrucciones
Ejemplo:

edad = 18

if edad >= 18:
   print ("Eres mayor de edad.")

En este ejemplo, si la variable edad es mayor o igual a 18,
se ejecutará el bloque de código dentro del if y se imprimirá el mensaje "Eres mayor de edad."

IF-ELSE
La estructura if-else nos permite especificar un bloque de código alternativo que se ejecutará si la condición del if es falsa.
La sintaxis básica es la siguiente:

edad = 15

if edad >= 18:
   print ("Eres mayor de edad.")

else:
   print ("eres menor de edad.")

En este ejemplo, si la variable edad es mayor o igual a 18, se ejecutará el bloque de código dentro del if y se imprimirá el mensaje "Eres mayor de edad."
De lo contrario, se ejecutará el bloque de código dentro del else y se imprimirá el mensaje "Eres menor de edad."

IF-ELIF-ELSE
La estructura if-elif-else nos permite especificar múltiples condiciones y bloques de código alternativos.
La sintaxis básica es la siguiente:

if condicion1:
   # Bloque de código a ejecutar si la condicion1 es verdadera
   instrucciones
elif condicion2:
   # Bloque de código a ejecutar si la condicion2 es verdadera
   instrucciones
else:
   # Bloque de código a ejecutar si ninguna condición anterior es verdadera
   instrucciones
Ejemplo:

calificacion = 85

if calificacion >= 90:
   print ("Excelente")

elif calificacion >= 80:
   print ("Muy bueno")

elif calificacion >= 70:
   print ("Bueno")

else:
   print ("Necesita mejorar")
