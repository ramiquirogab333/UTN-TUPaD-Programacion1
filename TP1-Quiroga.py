# TP1-Quiroga.py

#1
print("Hola Mundo!");

#2
nombre=input("¿Cuál es tu nombre? ");
print(f"Hola, {nombre}, un placer conocerte ");

#3
nombre=input("¿Cuál es tu nombre completo? ");
edad = int(input("¿Qué edad tenés? "));
lugar = input("¿Dónde vivís? ");
print(f"soy {nombre}, tengo {edad} años y vivo en {lugar}");

#4
radio = int(input("Ingrese el radio del círculo: "));
area = 3.14 * radio**2;
perimetro = 2 * 3.14 * radio;
print(f"El área del círculo es: {area}");
print(f"El perímetro del círculo es: {perimetro}");

#5
segundos=int(input("Ingrese una determinada cantidad de segundos para convertir a su equivalente en horas "));
horas = segundos / 3600;
print(f"{segundos} segundos son {horas} horas");

#6
numero = int(input("Ingrese un número: "));
print(f"La tabla de multiplicar de {numero} es:");
print(f"{numero} * 1 = {numero * 1}");
print(f"{numero} * 2 = {numero * 2}");
print(f"{numero} * 3 = {numero * 3}");
print(f"{numero} * 4 = {numero * 4}");
print(f"{numero} * 5 = {numero * 5}");
print(f"{numero} * 6 = {numero * 6}");
print(f"{numero} * 7 = {numero * 7}");
print(f"{numero} * 8 = {numero * 8}");
print(f"{numero} * 9 = {numero * 9}");
print(f"{numero} * 10 = {numero * 10}");

#7
print("A continuación se pedirán dos números, los cuales deben ser distintos a 0 para realizar distintas operaciones matemáticas")
numero1 = int(input("Ingrese número 1: "));
numero2 = int(input("Ingrese número 2: "));
print(f"{numero1} + {numero2} = {numero1 + numero2}");
print(f"{numero1} - {numero2} = {numero1 - numero2}");
print(f"{numero1} * {numero2} = {numero1 * numero2}");
print(f"{numero1} / {numero2} = {numero1 / numero2}");

#8
altura=float(input("Ingrese su altura en m: "));
peso=float(input("Ingrese su peso en kg: "));
imc = peso / (altura)**2;
print(f"Su IMC es: {imc}");

#9
temperatura=int(input("Ingrese temperatura actual en grados Celsius: "));
temperaturaFahrenheit = (temperatura * 9/5) + 32;
print(f"La temperatura en °F es: {temperaturaFahrenheit}");

#10
print("A continuación se solicitarán tres números para calcular el promedio")
numero1 = int(input("Primer número: "));
numero2 = int(input("Segundo número: "));
numero3 = int(input("Tercer número: "));
promedio = (numero1 + numero2 + numero3) / 3;
print(f"El promedio de los tres números es: {promedio}");