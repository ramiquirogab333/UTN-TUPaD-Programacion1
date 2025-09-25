alumnos = {}

for i in range(3):
    nombre = input(f"Nombre del alumno {i+1}: ")
    notas = []
    for n in range(3):
        nota = float(input(f"Ingresá la nota {i+1} del alumno {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

for alumno, notas in alumnos.items():
    promedio = sum(notas) / 9
    print(f"El alumno: {alumno} tiene un promedio de {promedio:.2f}") #Limito el promedio a 2 decimales con:.2f
