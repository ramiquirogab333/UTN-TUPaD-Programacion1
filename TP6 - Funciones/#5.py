def segundos_a_horas(segundos):
    horas = segundos // 3600
    print(f"{segundos} segundos equivalen a: {horas} hora(s).")

segundos = int(input("Ingrese cantidad de segundos para convertir a horas:\n"))
segundos_a_horas(segundos)