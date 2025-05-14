def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total
print(suma_variable(10, 25, 55))
print(suma_variable(100, 200, 450, 550, 1000))
