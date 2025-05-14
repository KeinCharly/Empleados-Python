frutas = ["Sandía", "Melón", "Pera", "Kiwi", "Mango"]
for fruta in frutas:
    print(fruta)

frutas.append("Aguacate")
print(frutas)

frutas.sort()
print(frutas)

frutas.insert(3, "Uvas")
print(frutas)

frutas.remove("Aguacate")
print(frutas)

fruta_eliminada = frutas.pop(1)
print(frutas)
print(fruta_eliminada)

frutas.reverse()
print(frutas)
