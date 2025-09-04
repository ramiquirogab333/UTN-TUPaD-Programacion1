
#9
cantidadNumeros = int(input("Ingrese la cantidad de números a cargar: "))

while cantidadNumeros < 1:
    print("INGRESE UNA CANTIDAD VALIDA")
    cantidadNumeros = int(input("Ingrese la cantidad de números a cargar: "))
sumatoria = 0

for i in range(cantidadNumeros):
    numero = int(input(f"Ingrese el número ({i+1}): "))
    sumatoria = sumatoria + numero

media = sumatoria/cantidadNumeros

print(f"La media de los números ingresados es: {media}")