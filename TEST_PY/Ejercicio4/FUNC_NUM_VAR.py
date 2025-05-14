def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total
print(suma_variable(5, 10, 30,))
print(suma_variable(11, 22, 44, 55))