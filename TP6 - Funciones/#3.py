def informacion_personal(nombre, apellido, edad, residencia):
 print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("¿Cómo te llamas?\n")
apellido = input("¿Cuál es tu apellido?\n")
edad = input("¿Cuál es tu edad?\n")
residencia = input("¿Dónde vivís?\n")
informacion_personal(nombre, apellido, edad, residencia)