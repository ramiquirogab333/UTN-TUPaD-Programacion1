paises = {
    "Argentina": "Buenos Aires",
    "España": "Madrid",
    "Uruguay": "Montevideo"
}

invertido = {}

for pais, capital in paises.items():
    invertido[capital] = pais

print("Diccionario original:", paises)
print("Diccionario invertido:", invertido)

      
