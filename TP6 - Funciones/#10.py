def calcular_promedio(a, b, c):
    promedio = (a+b+c)/3
    return promedio

print ("A continuación se solicitarán 3 números para calcular su promedio")
lista = []
for i in range(0,3):
    print(f"Ingrese el numero ({i+1}): ")
    num = int(input())
    lista.append(num)

a = lista[0]
b = lista[1]
c = lista[2]

print(f"Promedio calculado: {calcular_promedio(a,b,c):.2f}") #Limito el promedio a 2 decimales con :.2f