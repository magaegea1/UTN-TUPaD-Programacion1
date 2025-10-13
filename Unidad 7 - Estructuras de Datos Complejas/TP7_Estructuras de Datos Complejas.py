#Tp 7 - Estructuras de Datos Complejos - TUPaD
print("--- TP 7 - Estructuras de Datos Complejos ---\n")

#-------------------------------------------------------------------------
# Actividad 1. Dado el diccionario precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300 

print("_"*40, "\n")
print("¡Hola! Comenzamos con las Actividades 1, 2 y 3\n")

# Definir el diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

print(f"--- Actividad 1 ---\n")
print(f"Diccionario de precios de frutas original:\n   {precios_frutas}")
# Añadir las  frutas con sus respectivos precios:
precios_frutas ["Naranja"] = 1200
precios_frutas ["Manzana"] = 1500
precios_frutas ["Pera"] = 2300 

print(f"\nDiccionario de precios de frutas actualizado:\n   {precios_frutas}")


# Actividad 2. Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado 
# en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

# Añadir las  frutas con sus respectivos precios de la Actividad 2:
precios_frutas ["Banana"] = 1330
precios_frutas ["Manzana"] = 1700
precios_frutas ["Melón"] = 2800 

print(f"\n--- Actividade 2 ---\n")
print(f"Diccionario de precios de frutas actualizado:\n   {precios_frutas}")

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, 
# crear una lista que contenga únicamente las frutas sin los precios.

print(f"\n--- Actividade 3 ---\n")
frutas = list(precios_frutas.keys())
 
print(f"Lista de frutas:\n   {frutas}")

print("\n¡Muchas gracias y hasta luego!\n")

# Actividad 4. Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

print("_"*40, "\n")
print(f"Actividad 4\n")
print("¡Hola!\n")

# Crear el diccionario de la agenda vacío
agenda = {}

def solicitar_numero(nombre):
    valido=False
    while not valido:
        numero_texto=input(f"\n¿Cuál es el número de {nombre}?: ").strip()
        try:
            numero=int(numero_texto)
            valido=True
        except ValueError:
            print("Debes ingresar un número válido...")
    return numero

# Cargar 5 contactos con nombre como clave y número como valor
print("Vamos a agregar 5 contactos a la agenda\n")
contador=0
while contador < 5:
    valido=False

    #Solicitar el contacto al usuario
    nombre=input("¿Cuál es el nombre del contacto que querés agregar?: ").strip().title()
    while nombre=="":
        print("\nEl nombre no puede estar vacío, vuelve a intentarlo...")
        nombre=input("¿Cuál es el nombre del contacto que querés agregar?: ").strip().title()

    #Validar si es un contacto nuevo o uno para actualizar
    if nombre in agenda:
        actualizar=input(f"{nombre} ya está agendado, deseas actualizar su número? s/n: ").strip().lower()
        if actualizar == "s":
            numero=solicitar_numero(nombre)
            
        else:    
            print(f"No se actualizará el número de {nombre} \nContinuamos con la carga de otro contacto\n")
        valido=True

    #Solicitar el número al usuario para contactos nuevos
    if not valido:
        numero=solicitar_numero(nombre)
        #Agregar contacto al diccionario
        agenda[nombre]=numero
        contador+=1

print(agenda)

#Consultar contactos
salir=False
while not salir:
    consulta_agenda=input(f"\n¿Cuál contacto deseas ver? \nIndica su nombre: ").strip().title()
    while consulta_agenda=="":
        print("\nEl nombre no puede estar vacío, vuelve a intentarlo...")
        consulta_agenda=input(f"\n¿Cuál contacto deseas ver? \nIndica su nombre: ").strip().title()

    if consulta_agenda in agenda:
        print(f"{consulta_agenda}: {agenda[consulta_agenda]}")
    else:
        print("Ese contacto no se encuentra agendado")

    desea_salir=input("\n¿Deseas consultar algún otro contacto? s/n: ").strip().lower()
    if desea_salir!="s":
        print("Haz seleccionado salir")
        salir=True
             
print("\n¡Muchas gracias y hasta luego!\n")

# Actividad 5. Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

print("_"*40, "\n")
print(f"Actividad 5\n")
print("¡Hola!\n")

cantidad_palabras={}

frase=input(f"¿Cuál es la frase?: ").strip().title()
while frase=="":
    print("\nLa frase no puede estar vacía...")
    frase=input(f"¿Cuál es la frase?: ").strip().title()

palabras=frase.split()
set_frase=set(palabras)

print(f"\nLas palabras que aparecen en {frase} son: {set_frase}")

for palabra in set_frase:
    cont=0
    for elemento in palabras:
        if elemento==palabra:
            cont+=1
    cantidad_palabras[palabra]=cont

for palabra in sorted(cantidad_palabras):
    print(f"{palabra}: {cantidad_palabras[palabra]}")

print("\n¡Muchas gracias y hasta luego!\n")

# Actividad 6. Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno.

print("_"*40, "\n")
print(f"Actividad 6\n")
print("¡Hola!\n")

#Validación de que un valor sea un número

lista_completa_notas={}
promedios={}

def probar_numero(n):
    try: 
        n=float(n)
        return True
    except ValueError:
        return False

#Cacular promedio de cada estudiante
def calcular_promedio(lista):
    suma=0
    for nota in lista:
        suma+=nota
    return suma / len(lista)

# Solicitar los tres nombre y notas
for i in range(3):
    #Solicitar el nombre del alumno al usuario y validar que no esté vacio
    nombre=input("¿Cuál es el nombre del estudiante que querés agregar?: ").strip().title()
    while nombre=="":
        print("\nEl nombre no puede estar vacío, vuelve a intentarlo...")
        nombre=input("¿Cuál es el nombre del estudiante que querés agregar?: ").strip().title()
    
    #Solicitar las notas de cada alumno y armar la tupla
    lista_notas=[]
    for j in range(1,4):
        nota=-1
        while nota<1 or nota>10:
            nota_texto=input(f"Nota {j} de {nombre}: ").strip()
            while not probar_numero(nota_texto):
                print("\nDebes ingresar un valor numérico, intenta nuevamente...")
                nota_texto=input(f"Nota {j} de {nombre}: ").strip()
            nota=float(nota_texto)
            if nota<1 or nota>10:
                print("La nota debe ser un valor entre 1 y 10, intenta nuevamente...")
        lista_notas.append(nota)
    tupla_notas=tuple(lista_notas)

    #Armar un diccionario para guardar todas las notas correspondientes a cada estudiante
    lista_completa_notas[nombre]=tupla_notas
    print(f"\nLas notas de {nombre} son {tupla_notas}\n")
      
    #Calcular promedios y registrarlos en un diccionario:
    promedio=calcular_promedio(lista_notas)
    print(f"El promedio de las notas de {nombre} es {promedio:.2f}\n")

    promedios[nombre]=round(promedio,2)

#Mostrar los resultados
print(f"\nLas notas registradas son:")
for alumno, nota in lista_completa_notas.items():
    print(f"{alumno}: {nota} ")   
print(f"\nLos promedios registrados son:")  
for alumno, media in promedios.items():
    print(f"{alumno}: {media} ")

print("\n¡Muchas gracias y hasta luego!\n")

# Actividad 7. Dado dos sets de números, representando dos listas de estudiantes que 
# aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).  

print("_"*40, "\n")
print(f"Actividad 7\n")
print("¡Hola!\n")

#Se arman los dos set con los legajos de los estudiantes que aprobaron
parcial1={1023,1015,1025,1001,1008}
parcial2={1010,1015,1005,1001,1023,1008,1027}

print(f"Los que aprobaron el parcial 1 son:")
for aprobado1 in sorted(parcial1):
    print(f"{aprobado1}, ", end="")

print(f"\n\nLos que aprobaron el parcial 2 son:")
for aprobado2 in sorted(parcial2):
    print(f"{aprobado2}, ", end="")

# • Mostrá los que aprobaron ambos parciales.
aprobados_1y2=parcial1&parcial2
print(f"\n\nLos que aprobaron ambos parciales son:")
for aprobado1y2 in sorted(aprobados_1y2):
    print(f"{aprobado1y2}, ", end="")

# • Mostrá los que aprobaron solo uno de los dos.
aprobados_solo_uno=parcial1^parcial2
print(f"\n\nLos que aprobaron solo un parcial son:")
for aprobo1 in sorted(aprobados_solo_uno):
    print(f"{aprobo1}, ", end="")

# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).  
aprobados_al_menos_uno=parcial1|parcial2
print(f"\n\nLos que aprobaron al menos un parcial son:")
for aprobo_algo in sorted(aprobados_al_menos_uno):
    print(f"{aprobo_algo}, ", end="")

print("\n\n¡Muchas gracias y hasta luego!\n")

# Actividad 8. Armá un diccionario donde las claves sean nombres de productos y los valores 
# su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

print("_"*40, "\n")
print(f"Actividad 8\n")
print("¡Hola!")

inventario={"Alfajores":10, "Papas":15, "Gomitas":12, "Chocolate":7, "Nachos":0}

#Validación para espacio vacio
def vacio():
    frase=input().strip().title()
    while frase=="":
        print("Disculpa, no se ha ingresado nada, inténtalo de nuevo: ", end="")
        frase=input().strip().title()
    return frase

#Validación para el ingreso de números
def numero_valido():
    num=False
    while not num:
        num_texto=input().strip()
        try: 
            numero=int(num_texto)
            if 1<=numero<=1000:
                num=True
            else:
                print("\nDisculpa, debe ingresar un número entre 1 y 1000: ", end="")
        except ValueError:
            print("\nDisculpa, no se ha ingresado un número válido, inténtalo de nuevo: ", end="")

    return numero        
        
salir=False
# Presentar al usuario un menú de opciones
while not salir:    
    # Mostrar al usuario las opciones disponibles del menú
    print("\nElige el número de la opción deseada\n" \
    "1) Consultar el stock de un producto\n" \
    "2) Agregar unidades al stock si el producto ya existe en el inventario\n" \
    "3) Agregar un nuevo producto si no existe en el inventario.\n" \
    "4) Salir\n")

    # El usuario ingresa su elección
    print("¿Cuál es el número de la opción deseada? ", end="") 
    opcion_menu=vacio()   

    match opcion_menu:
        case "1":
            # • Consultar el stock de un producto ingresado.
            print("¿Qué producto querés consultar? ", end="")
            producto=vacio()
            if producto in inventario:
                print(f"{producto}: {inventario[producto]}")
            else:
                print(f"Disculpe, pero no disponemos de {producto} en el inventario")
                print("Estos son los productos disponibles en el inventario")
                for producto in sorted(inventario.keys()):
                    print(f"{producto}")
                        
            input("\nVolvemos al menú principal \nPresioná Enter para continuar...")

        case "2":
            # • Agregar unidades al stock si el producto ya existe.
            print("¿Qué producto querés agregar? ", end="")
            producto=vacio()
            if producto in inventario:
                print(f"En este momento hay {producto}: {inventario[producto]}")
                print(f"¿Cuántas unidades de {producto} querés agregar: ", end="")
                unidades=numero_valido()
                inventario[producto]+=unidades
                print(f"{producto}: {inventario[producto]}")
            else:
                print(f"Disculpe, pero no disponemos de {producto} en el inventario")

            input("\nVolvemos al menú principal \nPresioná Enter para continuar...")

        case "3":
            # • Agregar un nuevo producto si no existe.
            print("¿Qué producto nuevo querés agregar? ", end="")
            producto=vacio()
            if producto in inventario:
                print(f"Disculpe, pero ya existe {producto} en el inventario")

            else:
                print(f"¿Cuántas unidades de {producto} querés agregar: ", end="")
                unidades=numero_valido()
                inventario[producto]=unidades
                print(f"{producto}: {inventario[producto]}")

            input("\nVolvemos al menú principal \nPresioná Enter para continuar...")

        case "4":
            # Salir del menú.
            salir=True
            print("\nVamos al salir del sistema, estamos cerrando con el siguiente inventario:")
            for producto, unidad in sorted(inventario.items()):
                print(f"{producto}: {unidad}")

        case _:
            print("\nDisculpa, pero la opción ingresada no es válida")
            input("Volvemos al menú principal \nPresioná Enter para continuar...")

print("\n¡Muchas gracias y hasta luego!\n")

# Actividad 9. Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

print("_"*40, "\n")
print(f"Actividad 9\n")
print("¡Hola!")

from datetime import datetime

agenda = {
    ("Lunes", "10:00"): "Reunión de equipo",
    ("Martes", "15:00"): "Clase de programación",
    ("Miércoles", "08:00"): "Cita con el veterinario",
    ("Jueves", "18:00"): "Llevar a Micaela a clase de cerámica",    
    ("Viernes", "21:00"): "Video llamada con la abuela",
    ("Sábado", "13:00"): "Almuerzo con las chicas",
    ("Domingo", "09:30"): "Viene tu suegra"
}

#Validación dia y horario
dia_semana={"Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"}

def dia_valido():
    dia=input().strip().title()
    while dia not in dia_semana:
        print("No se ha ingresado un día de la semana, intenta nuevamente: ", end="")
        dia=input().strip().title()
    return dia

def hora_valida():
    while True:
        entrada=input("Ingresá la hora (formato HH:MM): ").strip()
        try:
            return datetime.strptime(entrada, "%H:%M").time()
        except ValueError:
            print("Formato incorrecto. Intentá con HH:MM (ejemplo: 09:45).")

# Permitir al usuario consultar qué actividad hay en cierto día y hora.
salir=False
while not salir:
    print("\n¿Qué día querés consultar? ", end="")
    dia_consulta=dia_valido()
    print("\n¿En qué horario? ")
    hora=hora_valida()
    horario=hora.strftime('%H:%M')

    #Mostrar resultado
    if (dia_consulta, horario) in agenda:
            print(f"El día {dia_consulta} a las {horario} tienes agendado: 📅 {agenda[(dia_consulta, horario)]} ")
    else:
        print(f"No hay ninguna actividad agendada para el {dia_consulta} a las {horario}")

    salida=input("¿Deseas consultar otro día y horario? (ingresa 'n' para salir): ").strip().lower()
    if salida=="n":
        salir=True        

print("\n¡Muchas gracias y hasta luego!\n")

# Actividad 10. Dado un diccionario que mapea nombres de países con sus capitales, 
# construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

print("_"*40, "\n")
print(f"Actividad 10\n")
print("¡Hola!\n")

paises_capitales={"Argentina":"Buenos Aires", "Canadá":"Toronto", "Senegal":"Dakar", "Tailandia":"Bangkok"}
capitales_paises={}

for pais, capital in paises_capitales.items():
    capitales_paises[capital]=pais

print("Diccionario original: Keys = Paises y Values = Capitales")
print(paises_capitales)

print("\nDiccionario nuevo (invertido): Keys = Capitales y Values = Paises")
print(capitales_paises)

print("\n¡Muchas gracias y hasta luego!\n")
