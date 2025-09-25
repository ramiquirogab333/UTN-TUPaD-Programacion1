frase = input("Ingrese una frase al azar: ")
palabras = frase.split()

unicas = set(palabras)
print("Palabras únicas:", unicas)

recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("Recuento de palabras:", recuento)