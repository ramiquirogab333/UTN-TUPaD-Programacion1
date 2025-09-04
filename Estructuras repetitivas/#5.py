#5
import random

numeroAzar = random.randint(0,9)
intentos = 0
num = -1
print("Adivina el número entre 0 y 9")

while num != numeroAzar:
    num = int(input("Ingrese un número: "))
    intentos += 1
    if num == numeroAzar:
        print(f"¡Ganaste, felicitaciones! Te tomó {intentos} intento/s adivinar el número.")
    else:
        print("Número incorrecto, intente de nuevo.")