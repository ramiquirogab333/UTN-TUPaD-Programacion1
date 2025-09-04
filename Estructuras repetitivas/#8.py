#8
cantidadNumeros = int(input("Ingrese la cantidad de numeros que quiere cargar: "))

positivos = 0
negativos = 0
pares = 0
impares = 0

while cantidadNumeros < 1:
    print("Error, ingrese una cantidad válida")
    cantidadNumeros = int(input("Ingrese la cantidad de números a cargar: "))

for i in range(cantidadNumeros):
    num = int(input(f"Ingrese número {i+1}:"))

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    
    if num%2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")