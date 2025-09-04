#10
numero = int(input("Ingrese un número: "))
numeroInvertido = 0

while numero >= 1:
    valor = numero % 10
    numero = int(numero/10)
    numeroInvertido = numeroInvertido*10 + valor

print(f"El número ingresado con los dígitos invertidos es: {numeroInvertido}")