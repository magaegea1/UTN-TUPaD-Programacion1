#Tp 6 - Funciones _ TUPaD
print("--- TP 6 - Funciones ---\n")

#-------------------------------------------------------------------------
# Actividad 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función 
# desde el programa principal.
print("_"*40, "\n")
print(f"Actividad 1 \n")

# Definir la función
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Llamar la función
imprimir_hola_mundo()

print("\n¡Muchas gracias y hasta luego!\n")

#-------------------------------------------------------------------------
#Actividad 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva 
# un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
# “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

print("_"*40, "\n")
print(f"Actividad 2 \n")

# Definir la función para saludar al usuario
def saludar_usuario(nombre):
    print (f"Hola {nombre}!\n")

# Pedir el nombre al usuario
tu_nombre=input("¿Cuál es tu nombre?\n   ").strip().title()

# Validar que la entrada no esté en blanco
while tu_nombre=="":
    print("Disculpa, pero la entrada no puede estar en blanco")
    tu_nombre=input("¿Cuál es tu nombre?\n   ").strip().title()

# Llamar a la función desde el programa principal
saludar_usuario(tu_nombre)

print("\n¡Muchas gracias y hasta luego!\n")

#-------------------------------------------------------------------------
#Actividad 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e 
# imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y 
# llamar a esta función con los valores ingresados.

print("_"*40, "\n")
print(f"Actividad 3\n")
print("¡Hola!")

def informacion_personal(nombre, apellido, edad, residencia):
    print (f"\nSoy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Pedir el nombre al usuario
tu_nombre=input("\n¿Cuál es tu nombre? ").strip().title()

# Validar que la entrada no esté en blanco
while tu_nombre=="":
    print("Disculpa, pero la entrada no puede estar en blanco")
    tu_nombre=input("\n¿Cuál es tu nombre? ").strip().title()

# Pedir el apellido al usuario
tu_apellido=input("\n¿Cuál es tu apellido? ").strip().title()

# Validar que la entrada no esté en blanco
while tu_apellido=="":
    print("Disculpa, pero la entrada no puede estar en blanco")
    tu_apellido=input("\n¿Cuál es tu apellido? ").strip().title()

# Pedir la edad al usuario
tu_edad=input("\n¿Cuál es tu edad (en números)? ").strip()

# Validar que la entrada no esté en blanco y que sea un número
while not tu_edad.isdigit():
    print("Disculpa, pero la entrada no es válida, debe ser un número.")
    tu_edad=input("\n¿Cuál es tu edad? ").strip()

# Pedir el lugar de residencia al usuario
tu_residencia=input("\n¿Cuál es tu lugar de residencia? ").strip().title()

# Validar que la entrada no esté en blanco
while tu_residencia=="":
    print("Disculpa, pero la entrada no puede estar en blanco")
    tu_residencia=input("\n¿Cuál es tu lugar de residencia? ").strip().title()

informacion_personal(tu_nombre, tu_apellido, tu_edad, tu_residencia)

print("\n¡Muchas gracias y hasta luego!\n")

#-------------------------------------------------------------------------
#Actividad 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados. 

print("_"*40, "\n")
print(f"Actividad 4\n")
print("¡Hola!\n")

# Para usar el valor de pi con precisión
import math

def calcular_area_circulo(radio):
    area_circulo=math.pi*radio**2
    return area_circulo


def calcular_perimetro_circulo(radio):
    perimetro_circulo=2*math.pi*radio
    return perimetro_circulo

# Pedir el radio al usuario y validarlo
valor_valido = False
while not valor_valido:
    tu_radio = input("¿Cuál es el radio del círculo? ").strip()
    try:
        tu_radio = float(tu_radio)
        valor_valido=True
    except ValueError:
        print("Debes ingresar un número válido (puede tener decimales).")

print(f"\nEl área del círculo es {calcular_area_circulo(tu_radio):.2f}")
print(f"\nEl perímetro del círculo es {calcular_perimetro_circulo(tu_radio):.2f}")


print("\n¡Muchas gracias y hasta luego!\n")

#-------------------------------------------------------------------------
# Actividad 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y 
# devuelva la cantidad de horas correspondientes. 
# Solicitar al usuario los segundos y mostrar el resultado usando esta función.

print("_"*40, "\n")
print(f"Actividad 5\n")
print("¡Hola!")

# Definición de la función para pasar segundos a horas
def segundos_a_horas(segundos):
    horas=segundos/3600
    return horas

# Pedir al usuario la cantidad de segundos y validar
hora_valida=False
while not hora_valida:
    segundos_usuario=input(f"\n¿Cuántos segundos querés pasar a horas: ").strip()
    try:
        segundos_usuario=float(segundos_usuario)
        hora_valida=True
    except ValueError:
        print("El valor ingresado no es válido")

# Mostrar el resultado
print(f"\n {segundos_usuario:.2f} segundos equivale a {segundos_a_horas(segundos_usuario):.2f} horas")
        

print("\n¡Muchas gracias y hasta luego!\n")

#-------------------------------------------------------------------------
#Actividad 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y 
# imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

print("_"*40, "\n")
print(f"Actividad 6\n")
print("¡Hola!\n")

# Definir la función para la tabla de multiplicar
def tabla_multiplicar(numero):
    print()
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero*(i)}")

# Pedir el número al usuario y validarlo
num_valido=False
while not num_valido:
    num=input("¿Cuál es el número del que querés saber la tabla (entre 1 y 100)?: ").strip()
    try:
        num=int(num)
        if num<=100 and num>=1:
            num_valido=True
        else:
            print("Elige un número entero entre 1 y 100 para que sea válido")
    except ValueError:
        print("El valor ingresado no es válido, debe ser un número entero")

# Mostrar el resultado
tabla_multiplicar(num)

print("\n¡Muchas gracias y hasta luego!\n")

#-------------------------------------------------------------------------
# Actividad 7. Crear una función llamada operaciones_basicas(a, b) que 
# reciba dos números como parámetros y devuelva una tupla con el resultado de 
# sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

print("_"*40, "\n")
print(f"Actividad 7\n")
print("¡Hola!\n")

print("Ingresa dos números enteros para realizar las cuatro operaciones básicas con ellos, deben estar en orden:")
# Definir la función
def operaciones_basicas(a, b):
    tupla=(a+b, a-b, a*b, a/b)
    return tupla

# Definir una función para limitar la cantidad de decimales
def tiene_demasiados_decimales(numero, max_decimales):
    texto_del_numero = str(numero)
    if "." in texto_del_numero:
        decimales = texto_del_numero.split(".")[1]
        return len(decimales) > max_decimales
    return False



# Pedir los números al usuario y validarlos
num1_valido=False
num2_valido=False
while not num1_valido or not num2_valido:

    # Pedir al usuario el primer número y validarlo
    if not num1_valido:
        num1=input("\nIngresa el primer número (será el sumando, minuendo, factor y dividendo según cada caso): ").strip()
        try:
            num1=float(num1)
            # Validar que no sea demasiado grande o pequeño
            if abs(num1) < 1e-6 or abs(num1) > 1e6 or tiene_demasiados_decimales(num1, 6):
                print(f"El número {round(num1, 6)} tiene demasiadas cifras para esta actividad")
                print("Debes elegir un número entre 0.000001 y 1000000, y con un máximo de 6 decimales")
                print("Observa que el '.' (punto) es el separador de decimales")
            else: 
                num1_valido=True
        # Validar que sea un número        
        except ValueError:
            print("El primer número ingresado no es válido, debe ser un número. \nIntente nuevamente.")

    # Pedir al usuario el segundo número y validarlo        
    elif not num2_valido:
        num2=input("\nIngresa el segundo número (será el sumando, sustraendo, factor y divisor según cada caso): ").strip()
        try:
            num2=float(num2)
            # Validar que no sea 0
            if num2==0:
                print ("No se puede dividir entre cero, debes elegir otro segundo número")
            # Validar que no sea demasiado grande o pequeño    
            elif abs(num2) < 1e-6 or abs(num2) > 1e6 or tiene_demasiados_decimales(num2, 6):
                print(f"El número {round(num2, 6)} tiene demasiadas cifras para esta actividad")
                print("Debes elegir un número entre 0.000001 y 1000000, y con un máximo de 6 decimales")
                print("Observa que el '.' (punto) es el separador de decimales")
            else:
                num2_valido=True
        # Validar que sea un número
        except ValueError:
            print("El segundo número ingresado no es válido, debe ser un número. \nIntente nuevamente.")

# Llamar a la función y mostrar los resultados al usuario
resultado=operaciones_basicas(num1, num2)
print("\nMuchas gracias, a continuación podrás ver los resultados: ")
print(f"El resultado de sumar (redondeado a dos decimales) {num1} + {num2} es {resultado[0]:.2f}")
print(f"El resultado de restar (redondeado a dos decimales) {num1} - {num2} es {resultado[1]:.2f}")
print(f"El resultado de multplicar (redondeado a dos decimales) {num1} x {num2} es {resultado[2]:.2f}")
print(f"El resultado de dividir (redondeado a dos decimales) {num1} / {num2} es {resultado[3]:.2f}")

print("\n¡Muchas gracias y hasta luego!\n")

#-------------------------------------------------------------------------
# Actividad 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, 
# y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para 
# mostrar el resultado con dos decimales.

print("_"*40, "\n")
print(f"Actividad 8\n")
print("¡Hola!\n")

# Definir la función para calcular el IMC, peso en kilos y altura en metros
def calcular_imc(peso, altura):
    imc=peso/(altura**2)
    return imc

print("Vamos a calcular el IMC, para ello necesitaremos el peso en kilogramos y la altura en metros")

# Pedir al usuario el peso y validarlo
peso_valido=False
while not peso_valido:
    peso_ingresado=input(f"\nIngresa el peso, debe ser un número entre 10 y 500 kg: ")
    try:
        peso_ingresado=float(peso_ingresado)
        if peso_ingresado < 10 or peso_ingresado > 500:
            print("El peso ingresado no es válido para esta actividad.")
            print("Elegí un valor entre 10 y 500 kg. Este rango permite cuidar la coherencia sin excluir cuerpos reales.")
        else:
            peso_valido=True
    except ValueError:
        print("Debes ingresar un número entre 10 y 500 para que sea un peso válido")

# Pedir al usuario la altura y validarlo
altura_valida=False
while not altura_valida:
    altura_ingresada=input(f"\nIngresa la altura, debe ser un número entre 0.4 y 2.8 metros: ")
    try:
        altura_ingresada=float(altura_ingresada)
        if altura_ingresada < 0.4 or altura_ingresada > 2.8:
            print("La altura ingresada no es válida para esta actividad.")
            print("Elegí un valor entre entre 0.4 y 2.8 metros. Este rango permite cuidar la coherencia sin excluir cuerpos reales.")
        else:
            altura_valida=True
    except ValueError:
        print("Debes ingresar un número entre 0.4 y 2.8 para que sea una altura válida")

# Mostrar al usuario el IMC
print(f"\nEl IMC, tomando en cuenta el peso: {peso_ingresado:.2f} Kg y la altura: {altura_ingresada} metros")
print(f"es de: {calcular_imc(peso_ingresado,altura_ingresada):.2f}" )

print("\n¡Muchas gracias y hasta luego!\n")

#-------------------------------------------------------------------------
# Actividad 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura 
# en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

print("_"*40, "\n")
print(f"Actividad 9\n")
print("¡Hola!\n")

#Definir la función para pasar a fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit

print("Vamos a pasar grados celsius a fahrenheit")

# Pedir al usuario los grados celsius y validar
celsius_valido=False
while not celsius_valido:
    celsius_ingresado=input("\nIngresa los grados celsius (sólo números): ").strip()
    try:
        celsius_ingresado=float(celsius_ingresado)
        if celsius_ingresado<-273.15 or celsius_ingresado>1000:
            print(f"Has ingresado {celsius_ingresado}, para que sea válido debe ser un número real, entre -273.15°C y 1000°C")
        else:
            celsius_valido=True
    except ValueError:
        print("Debes ingresar un número para que sea válido")

# Mostrar el resultado al usuario
print(f"{celsius_ingresado:.2f}°C equivalen a {celsius_a_fahrenheit(celsius_ingresado):.2f}°F")

print("\n¡Muchas gracias y hasta luego!\n")

#-------------------------------------------------------------------------
# Actividad 10. Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.

print("_"*40, "\n")
print(f"Actividad 10\n")
print("¡Hola!\n")

# Definir la función de calcular el promedio de 3 números
def calcular_promedio(a, b, c):
    promedio=(a+b+c)/3
    return promedio

# Función para validar los números
def num_valido(numero):
    valido=False
    while not valido:
        entrada=input(f"\nIngresa el {numero}: ").strip()
        try:
            num=float(entrada)
            if -1000<=num<=1000:
                valido=True
            else:
                print(f"El número {num} no está dentro del rango solicitado, debe ser entre -1000 y 1000")
        
        except ValueError:
            print(f"No has ingresado un número válido, intenta de nuevo")
    return num

# Solicitar tres números al usuario para calcular el promedio y validarlos

print("A continuación te pediremos 3 números para calcular su promedio, deben ser números entre -1000 y 1000")

num1=num_valido("primer número")
num2=num_valido("segundo número")
num3=num_valido("tercer número")

print(f"\nEl promedio entre los números \n{num1} \n{num2} \n{num3}") 
print(f"\n      es {calcular_promedio(num1, num2, num3):.2f} (redondeado a dos decimales)")

print("\n¡Muchas gracias y hasta luego!\n")
