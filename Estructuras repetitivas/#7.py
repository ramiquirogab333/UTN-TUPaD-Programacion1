#7
num = int(input("Ingrese número para calcular la suma de todos sus valores previos: "))

while num < 1:
    print("El valor no puede ser menor a 0")
    num = int(input("Ingrese el valor nuevamente: "))

sumaNumeros = 0

for i in range(0,num+1): 
    sumaNumeros = sumaNumeros + i

print(f"La suma de los números comprendidos entre 0 y {num} es de: {sumaNumeros}")