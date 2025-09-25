guia_telefonica = {}
for i in range(5):
  nombre = input("Ingrese el nombre del contacto: ")
  telefono = input("Ingrese el número de teléfono: ")
  guia_telefonica[nombre] = telefono

buscador = input("Ingrese nombre del contacto a buscar: ")
if buscador in guia_telefonica:
  print(f"El número de teléfono del contacto buscado es: ",(guia_telefonica[buscador]))
else:
 print("El contacto ingresado no está en la guía")

