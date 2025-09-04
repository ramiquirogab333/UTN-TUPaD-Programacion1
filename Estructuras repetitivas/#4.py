#4
num = 1
sumaNumeros = 0

while num != 0:
    num = int(input("Ingrese un número a la sumatoria o coloque 0 para salir: "))
    sumaNumeros = sumaNumeros + num

print(f"La sumatoria de los números ingresados es: {sumaNumeros}")