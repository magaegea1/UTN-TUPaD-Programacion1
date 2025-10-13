# Actividad 1
print("Actividad 1")
# Imprimir Hola Mundo! en pantalla
print("Hola Mundo!")
print()

# Actividad 2
print("Actividad 2")
# Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. 
# Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”.
nombre = input("¡Hola! ¿Cuál es tu nombre?: ")
print(f"Hola {nombre}")
print()

# Actividad 3
print("Actividad 3")
# Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia 
# e imprima por pantalla una oración con los datos ingresados
nombre = input("¡Hola! ¿Cuál es tu nombre?: ")
apellido = input("¿Cuál es tu apellido?: ")
edad = input("¿Cuántos años tienes?: ")
lugarDeResidencia = input("¿Dónde vives?: ")
print(f"Hola, eres {nombre} {apellido}, tenés {edad} y vives en {lugarDeResidencia}")
print()

# Actividad 4
print("Actividad 4")
# Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro. 
radio = float(input("¡Hola! ¿Cuál es el radio?: "))
areaCirculo=3.141516*radio**2
print(f"Hola,  El área del círculo de radio {radio} es {areaCirculo}")
print()

# Actividad 5
print("Actividad 5")
# Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale. segundos = int(input("¡Hola! ¿Cuál es la cantidad de sengundos que querés pasar a horas?: "))
segundos=float(input("Cuántos segundos querés pasar a horas:"))
horas=segundos/60/60
print(f"Hola, {segundos} segundos equivale a {horas} horas")
print()


# Actividad 6
print("Actividad 6")
# Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.   
numero = int(input("¡Hola! Querés saber la tabla del: "))
print(f"{numero} x 1 = {numero*1}")
print(f"{numero} x 2 = {numero*2}")
print(f"{numero} x 3 = {numero*3}")
print(f"{numero} x 4 = {numero*4}")
print(f"{numero} x 5 = {numero*5}")
print(f"{numero} x 6 = {numero*6}")
print(f"{numero} x 7 = {numero*7}")
print(f"{numero} x 8 = {numero*8}")
print(f"{numero} x 9 = {numero*9}")
print(f"{numero} x 10 = {numero*10}")
print()

# Actividad 7
print("Actividad 7")
# Crear un programa que pida al usuario dos números enteros distintos del 0 y 
# muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.    
numero1 = int(input("¡Hola! Escribe un número entero mayor que cero: "))
numero2 = int(input("¡Hola! Escribe otro número entero mayor que cero: "))
print(f"{numero1} + {numero2} = {numero1+numero2}")
print(f"{numero1} - {numero2} = {numero1-numero2}")
print(f"{numero1} x {numero2} = {numero1*numero2}")
print(f"{numero1} / {numero2} = {numero1/numero2}")
print()

# Actividad 8
print("Actividad 8")
# Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
peso = float(input("¡Hola! ¿Cuál es tu peso (en Kg)?: "))
altura = float(input("¡Hola! ¿Cuál es tu altura (en metros)?: "))
print(f"Tu IMC es {peso/altura**2}")
print()

# Actividad 9
print("Actividad 9")
# Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
celsius = float(input("¡Hola! ¿Cuál es la temperatura (en grados Celsius)?: "))
print(f"{celsius} grados Celsius equivalen a {celsius*9/5+32} grados Fahrenheit")
print()


# Actividad 10
print("Actividad 10")
# Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de dichos números. 
numero1 = float(input("¡Hola! ¿Cuál es el primer número?: "))
numero2 = float(input("¡Hola! ¿Cuál es el segundo número?: "))
numero3 = float(input("¡Hola! ¿Cuál es el tercer número?: "))
print(f"El promedio entre {numero1}, {numero2} y {numero3} es {(numero1+numero2+numero3)/3}")
