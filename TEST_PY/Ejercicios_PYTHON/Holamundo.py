def saludo(nombre):
    print(f"¡Hola, {nombre}!")
saludo("Charly")

def saludo():
    print("¡Hello, World!")
saludo()

def suma(a, b):
    return a+b

resultado = suma(3, 4)
print(resultado)

cuadrado = lambda x: x ** 2
print(cuadrado(5))

def funcion():
    variable_local=10
    print(variable_local)
variable_global=20
variable_local=10
def funcion2():
    print(variable_global)
funcion()
funcion2()
print(variable_global)
print(variable_local)

def calcular_media(*numeros):
    suma=sum(numeros)
    cantidad=len(numeros)
    media=suma/cantidad
    return media
print("Media:", calcular_media(10,20,30,40))

def sumar_3(x):
    return x+3
sumar=lambda x: x+3
print("sumarle 3 a un numero:", sumar(5))
