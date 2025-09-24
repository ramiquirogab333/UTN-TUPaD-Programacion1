def operaciones_basicas(a, b):
 tupla_operaciones = (a + b, a - b, a * b, a / b)
 print(f"Suma: {a} + {b} =  {tupla_operaciones[0]}")
 print(f"Resta: {a} - {b} =  {tupla_operaciones[1]}")
 print(f"Multiplicación: {a} * {b} =  {tupla_operaciones[2]}")
 print(f"División: {a} / {b} =  {tupla_operaciones[3]}")

print("A continuación se pedirán dos números para realizar operaciones básicas entre si")
numero_1 = int(input("Ingrese el primer número:\n"))
numero_2 = int(input("Ingrese el segundo número:\n"))
operaciones_basicas(numero_1, numero_2)