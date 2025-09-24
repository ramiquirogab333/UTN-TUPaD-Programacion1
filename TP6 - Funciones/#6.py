def tabla_multiplicar(numero):
  print(f"Tabla de multiplicar del {numero}:")
  for i in range(1,11):
    producto = numero * i
    print(f"{numero} x {i} = {producto}")

numero = int(input("Ingrese un número para calcular su tabla de multiplicar:\n"))
tabla_multiplicar(numero)