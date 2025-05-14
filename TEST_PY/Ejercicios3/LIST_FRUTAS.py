frutas = ["Sandía", "Mango", "Piña", "Kiwi", "Melón"]
for fruta in frutas:
    print(fruta)
frutas.append("Aguacate")
print(frutas)
frutas.insert(1, "Uvas")
print(frutas)
frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)
frutas.remove("Piña")
print(frutas)
fruta_eliminada = frutas.pop(0)
print(frutas)

