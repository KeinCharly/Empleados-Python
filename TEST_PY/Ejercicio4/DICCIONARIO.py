persona = {"Nombre": "Rupert Cowalsky", "Edad": 65, "Ciudad": "Germany"}
print(persona["Nombre"])
print(persona["Edad"])
print(persona["Ciudad"])

print(persona.keys())
print(persona.values())
print(persona.items())

persona.update({"Profesión": "Ingeniero Aeroespacial"})
print(persona)