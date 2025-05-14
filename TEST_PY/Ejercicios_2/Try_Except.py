try:
    resultado = 10/0
    print(resultado)
except ZeroDivisionError:
    print("Error: División por Cero")
except ValueError:
    print("Error: Valor inválido")