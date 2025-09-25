agenda = {
    ("lunes", "7:00"): "cursado",
    ("martes", "18:00"): "entrenar",
    ("jueves", "8:00"): "trabajar"
}

dia = input("Ingrese el día: ").lower()
hora = input("Ingrese la hora (ej: 10:00): ")

fecha = (dia, hora)

if fecha in agenda:
    print(f"Actividad: {agenda[fecha]}")
else:
    print("Actualmente no hay actividades programadas en la agenda")