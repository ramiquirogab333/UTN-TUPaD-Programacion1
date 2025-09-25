productos = {
   "chocolates": 10,
    "chupetines": 20,
    "chicles": 30,
    "carameleos": 100,
    "alfajores": 25
}

consulta_stock = input("Ingrese producto para consultar su stock: ")

print(f"Stock disponible de {consulta_stock}: {productos[consulta_stock]} unidades")
agregar_stock = input(f"Desea agregar {consulta_stock}? s/n ")

if agregar_stock == "s":
  cantidad = int(input("Cantidad a agregar: "))
  productos[consulta_stock] = cantidad
  print("Stock actualizado con éxito!")

agregar_prod = input("Desea agregar algún producto al catálogo? s/n")
if agregar_stock == "s":
  nuevo_prod = (input("Producto a agregar: "))
  cantidad = int(input("Cantidad a agregar: "))
  productos[nuevo_prod] = cantidad
  print("Producto agregado con éxito!")
   

