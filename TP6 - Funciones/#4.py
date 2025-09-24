import math

def calcular_area_circulo(radio):
    return math.pi*radio**2

def calcular_perimetro_circulo(radio):
    return 2*math.pi*radio

radio = float(input("Ingrese el radio del círculo: "))

print("El área del círculo es: ",calcular_area_circulo(radio))
print("El perímetro del círculo es: ",calcular_perimetro_circulo(radio))