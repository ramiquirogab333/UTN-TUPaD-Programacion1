#2
numero = int(input("Ingrese un número entero: "))
contador = 0
condicion = numero
while condicion >= 1:
    condicion = int(condicion/10)
    contador += 1
print(f"El número {numero} tiene {contador} dígito/s")