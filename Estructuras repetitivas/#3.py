#Punto 3
inicio = int(input("Ingrese el valor de inicio: "))
final = int(input("Ingrese el valor final: "))

while final < inicio:
    print("El valor final debe ser mayor que el valor de inicio.")
    final = int(input("Ingrese el valor final: "))

sumaNumeros = 0

for i in range(inicio+1,final):
    sumaNumeros += i

print(f"La suma de los números enteros comprendidos entre {inicio} y {final} es de: {sumaNumeros}")