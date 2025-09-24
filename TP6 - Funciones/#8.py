def  calcular_imc(peso, altura):
    IMC = peso/altura**2
    return IMC

peso = float(input("Ingrese su peso en kilogramos(kg): "))
altura = float(input("Ingrese su altura el metros(m): "))

print(f"Su IMC es de: {calcular_imc(peso,altura):.2f}") #Utilizo :.2f para limitar a 2 decimales