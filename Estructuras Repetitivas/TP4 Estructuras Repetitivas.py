print("TP Estructuras Repetitivas\n")

print("Actividad 1")
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
print("¡👋 Hola!")
for i in range (101):
    print(i)
print("¡Hasta Luego 👋!")


print("\nActividad 2")
# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
print("¡👋 Hola!")
numero=int(input("Por favor, ingresa un número entero, luego te diré cuántas cifras tiene: "))
sinSigno=abs(numero)
cifras=len(str(sinSigno))
print(f"El número {numero} tiene {cifras} cifras")
print("¡Hasta Luego 👋!")

print("\nActividad 3")
# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
print("¡👋 Hola! Vamos a sumar todos los números comprendidos entre dos valores")
num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))
sumatoria = 0

if num1 < num2:
    for i in range(num1 + 1, num2):
        sumatoria += i
elif num2 < num1:
    for j in range(num2 + 1, num1):
        sumatoria += j
else:
    sumatoria = 0
    print(f"No hay ningún número entre {num1} y {num2}, la sumatoria es 0")

print(f"La sumatoria de todos los números entre {num1} y {num2} es igual a: {sumatoria}")
print("¡Hasta Luego 👋!")

print("\nActividad 4")
# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
print("¡👋 Hola!\nVamos a sumar todos los números que ingreses, cuando quieras salir ingresa el cero\n")
num=int(input("Ingresa el primer número entero: "))
sumatoria=0
while num!=0:
    sumatoria += num
    num=int(input("Ingresa el siguiente número entero: "))
print(f"El total acumulado de todos los números ingresados es: {sumatoria}")
print("Hasta Luego 👋")

print("\nActividad 5")
#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
print("👋 Hola")
print("Frente a vos hay 10 puertas, con números del 0 al 9, debes elegir una de ellas para poder salir\n")
import random
aleatorio=random.randint(0,9)
num=int(input("¿Qué puerta elijes primero? "))
intentos=1
while num!=aleatorio:
    if num>-1 and num<10:    
        intentos+=1
        num=int(input("¡Oh no! ¡Puerta equivocada... \n Intenta de nuevo... elije una puerta: "))
    else:
        num=int(input("Esa puerta no existe, has gastado un intento 😱\ndebes elegir una de las disponibles: del 0 al 9: "))
        intentos+=1
print(f"\n✨✨✨¡¡¡Felicitaciones!!! ¡¡¡Lograste escapar luego de {intentos} intentos!!!✨✨✨\n...\n")
print("... Ahora... 🚨🚨🚨 C O R R E 🚨🚨🚨\n🚷🚨🐶 alguien olvidó atar al perro 🐶🚨🚷")
print("Suerte y hasta la próxima👋 ")

print("\nActividad 6")
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
print("¡👋 Hola!\n") #Para generar un salto más de línea antes del conteo, para que se vea más prolijo
for i in range (100,0,-2):
    print(i, end=" - ")
print(0) # Se imprime de este modo el último número para que no quede un guión al final del conteo
print("\n¡Hasta Luego 👋!")


print("\nActividad 7")
# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
print("¡👋 Hola!\nVamos a sumar todos los números enteros positivos desde cero hasta el número que elijas")
sumatoria=0
num=int(input("\nElije un número entero positivo: "))

while num<=0:
    num=int(input(" 😕\n¡¡¡El número no es positivo!!!\nElije un número entero positivo: "))

for i in range(1,num+1): #Desde 1 porque ya sumatoria vale 0
    sumatoria+=i

print(f"\nLa sumatoria desde 0 hasta {num} es: {sumatoria}")
print("¡Hasta Luego 👋!")


print("\nActividad 8")
#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
print("¡👋 Hola!")
print("A continuación voy a pedirte que ingreses 100 números enteros")
print("Al finalizar te diré cuántos de ellos son positivos, negativos, pares e impares\n")
cantidad=100
positivo=0
negativo=0
par=0
impar=0
for i in range(1,cantidad+1): #Se comienza en 1 por una cuestión estetética en la numeración posterior
    num=int(input(f"{i}° Número: "))
    if num%2==0:
        par+=1
        if num<0:
            negativo+=1
        elif num>0:
            positivo+=1
    else:
        impar+=1
        if num<0:
            negativo+=1
        elif num>0:
            positivo+=1

print("\nGracias 😎 \nDe los números ingresados tenemos:\n")
print(f"Ingresaste {positivo} números positivos")
print(f"Ingresaste {negativo} números negativos")
print(f"Ingresaste {par} números pares")
print(f"Ingresaste {impar} números impares")
print("\n¡Hasta Luego 👋!")


print("\nActividad 9")
# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
print("¡👋 Hola!")
print("A continuación voy a pedirte que ingreses 100 números enteros, luego te diré cuál es la media o promedio de ellos:\n")
cantidad=100
sumatoria=0
promedio=0
for i in range(1,cantidad+1): #Se comienza en 1 por una cuestión estetética en la numeración posterior
    num=int(input(f"{i}° Número: "))
    sumatoria+=num
media=sumatoria/cantidad
print(f"La media de los números ingresados es {media}")
print("\n¡Hasta Luego 👋!")


print("\nActividad 10")
# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
print("¡👋 Hola!")
print("\nA continuación te pediré un número entero para poder invertir sus cifras")
num=int(input("Ingresa el número: "))
numPositivo=abs(num)
cifras=int(len(str(numPositivo)))

print("\n Número invertido: ", end="")

if num<0:
    print("-", end="")

for i in range (cifras):
    print(numPositivo%10, end="")
    numPositivo=numPositivo//10

print(" 🪄")
print("\n¡Hasta Luego 👋!")

