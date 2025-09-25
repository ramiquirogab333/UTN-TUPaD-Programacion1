parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7, 8}

promocion = parcial1 & parcial2
regulares = parcial1 ^ parcial2
cantidad_regulares = parcial1 | parcial2

print("Aprobaron ambos:", promocion)
print("Aprobaron solo uno:", regulares)
print("Aprobaron al menos uno:", cantidad_regulares)