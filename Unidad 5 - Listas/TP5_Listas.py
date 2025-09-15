# 1) Crear una lista con las notas de 10 estudiantes.
#    • Mostrar la lista completa.
#    • Calcular y mostrar el promedio.
#    • Indicar la nota más alta y la más baja.

print(f"Actividad 1 \n")
print("¡Hola!\n")
notas=[5,6,4,8,9,10,7,8,6,10]
promedio=0
suma=0
cantidad_notas=len(notas)
nota_mayor=notas[0]
nota_menor=notas[0]

# Mostrar las notas de los estudiantes usando estructuras repetitivas con el "for" siguiente
print("Las notas de los 10 estudiantes son: ")

# Cálculo de promedio y de las nota mayor y menor
for nota in notas: 
    print(nota)
    suma+=nota
    
    if nota>=nota_mayor:
        nota_mayor=nota
        
    if nota<=nota_menor:
        nota_menor=nota    
    
promedio=suma/cantidad_notas
print(f"\nLa mayor nota obtenida fue {nota_mayor} y la menor {nota_menor}")
print(f"El promedio de las notas es: {promedio}")
print(f"\n¡Hasta Luego!")

# 2) Pedir al usuario que cargue 5 productos en una lista.
#   • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#   • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

print(f"Actividad 2 \n")
print("¡Hola!\n")
lista=[]
cantidad_productos=5
eliminar=0

# Pedir al usuario que cargue los 5 productos
print("Por favor, ingresa los productos que desea comprar")
for i in range (cantidad_productos):
    lista.append(str(input("Producto: ")))

# Crear una nueva lista con los 5 productos ordenados
print("\nLista ordenada alfabéticamente:")
lista_ordenada=sorted(lista)
for producto in lista_ordenada:
    print(producto)

# Preguntar al usuario si desea eliminar algún producto, si desea hacerlo entonces hacerlo, sino continuar 
while eliminar==0:
    eliminar=int(input(f"Selecciona si deseas eliminar alguno de los productos (Sí=0 y No=1) "))

    # y Verificar que el usuario haya ingresa una opción valida

    while eliminar!=0 and eliminar!=1:
        print("La opción ingresada no es válida, intente nuevamente:")
        eliminar=int(input(f"Selecciona si deseas eliminar alguno de los productos (Sí=0 y No=1) "))   
    # Eliminar el producto deseado       
    if eliminar==0:
        lista_ordenada.remove(str(input("Ingresa el producto que deseas eliminar: ")))
    
        print("\nLa nueva lista de productos es:")    
        for producto in lista_ordenada:
            print(producto)
    
print("\n¡Muchas gracias y hasta luego!")

# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#   • Crear una lista con los pares y otra con los impares.
#   • Mostrar cuántos números tiene cada lista.

print(f"Actividad 3\n")
print("¡Hola!\n")

lista=[]
lista_pares=[]
lista_impares=[]
import random
print("Estos son los 15 números enteros generados al azar entre 1 y 100")
# Armar una lista con los números al azar e imprmirla,
# Luego armar la lista con números los números pares y otra con los impares
for i in range (15):
    numero = random.randint(1, 100)  
    lista.append(numero)
    print(lista[i])
    if numero%2==0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

# Imprimir las listas pares e impares
print(f"\nHay en total {len(lista_pares)} números pares, y estos son:")
for par in lista_pares:
    print(par)
print(f"\nHay en total {len(lista_impares)} números impares, y estos son:")
for impar in lista_impares:
    print(impar)
print("\n¡Muchas gracias y hasta luego!")

# 4) Dada una lista con valores repetidos: 
#   • Crear una nueva lista sin elementos repetidos.
#   • Mostrar el resultado.

print(f"Actividad 4\n")
print("¡Hola!")

lista=[1,3,5,3,7,1,9,5,3]    
sin_repetidos=[]

# Armar la lista sin repetidos
for numero in lista:
    if numero not in sin_repetidos:
        sin_repetidos.append(numero)


#Imprimir en pantalla el resultado
print("\n La lista original de números:")
for i in lista:
    print(i)

print("\n La lista sin números repetidos:")
for j in sin_repetidos:
    print(j)

print("\n¡Muchas gracias y hasta luego!")

# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
#   • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#   • Mostrar la lista final actualizada.

print(f"Actividad 5\n")
print("¡Hola!")

estudiantes=["Ana","Emma","Hugo","Lisa","Norma","Pedro","Lucía","Bruno"]    
accion=""
# Mostrar la lista 
print("\nEstos son los estudiantes actualmente: ")
for nombre in estudiantes:
    print(nombre)

# Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente
accion = int(input("¿Querés agregar o eliminar un estudiante?\nEscribí 1 para agregar,  2 para eliminar o cualquier número para terminar: "))

while (accion==1 or accion==2):
    if accion==2:
        nombre = input("Por favor, escribí el nombre a eliminar: ")
        if nombre in estudiantes:
            estudiantes.remove(nombre)
        else:
            print("Ese nombre no está en la lista.")

    else:
        estudiantes.append(input("Por favor, agrega el nombre: "))
    accion = int(input("¿Querés agregar o eliminar algún estudiante más?\nEscribí 1 para agregar,  2 para eliminar o cualquier número para terminar: "))

# Mostrar la lista actualizada
print("\nEsta es la lista actualizada de estudiantes: ")
for nombre in estudiantes:
    print(nombre)


print("\n¡Muchas gracias y hasta luego!")

# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

print(f"Actividad 6\n")
print("¡Hola!")

lista=[1,2,3,4,5,6,7]    
lista_nueva=[]

# Mostrar la lista 
print("\nLista de números: ")
for numero in lista:
    print(numero)

lista_nueva.append(lista[-1]) # Agrega el último elemento

# Rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).
for i in range(len(lista) - 1):
    lista_nueva.append(lista[i]) # Agrega los demás elementos en orden


# Mostrar la lista actualizada
print("\nEsta es la lista actualizada: ")
for numero in lista_nueva:
    print(numero)


print("\n¡Muchas gracias y hasta luego!")

# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana. 
#   • Calcular el promedio de las mínimas y el de las máximas. 
#   • Mostrar en qué día se registró la mayor amplitud térmica.

print(f"Actividad 7\n")
print("¡Hola!")

matriz_temperaturas=[
    [12, 22],  # Día 1
    [14, 25],  # Día 2
    [10, 20],  # Día 3
    [13, 24],  # Día 4
    [11, 21],  # Día 5
    [15, 26],  # Día 6
    [12, 23]   # Día 7
]

# Variables a usar
suma_min=0
suma_max=0
promedioMin=0
promedioMax=0
TemperaturaMin=matriz_temperaturas[0][0]
TemperaturaMax=matriz_temperaturas[0][1]
mayorAmplitud=0
amplitud=0
diaMayorAmplitud=0
filas=len(matriz_temperaturas)

# Temperaturas mínimas 
print("\nLas temperaturas Mínimas regitradas son: ")
for i in range(filas):
    suma_min+=matriz_temperaturas[i][0] # Sumatoria de temperaturas mínimas
    print(matriz_temperaturas[i][0])

    if TemperaturaMin>=matriz_temperaturas[i][0]: #Calculo de Temperatura Mínima menor
        TemperaturaMin=matriz_temperaturas[i][0]

promedioMin=suma_min/filas # Promedio Temperaturas mínimas
print(f"\n El promedio de las temperaturas mínimas es: {promedioMin}")

# Temperaturas máximas 
print("\nLas temperaturas Máximas regitradas son: ")
for i in range(filas):
    suma_max+=matriz_temperaturas[i][1] # Sumatoria de temperaturas máximas
    print(matriz_temperaturas[i][1])

    if TemperaturaMax<=matriz_temperaturas[i][1]: #Calculo de Temperatura Mínima menor
        TemperaturaMax=matriz_temperaturas[i][1]

promedioMax=suma_max/filas # Promedio Temperaturas máximas
print(f"\nEl promedio de las temperaturas máximas es: {promedioMax}")

# Mostrar Temperaturas Máximas y Mínimas absolutas (no lo pide el ejercicio pero se deja para mayores referencias)

print(f"\nLa temperatura mínima registrada es {TemperaturaMin} y la máxima registrada es {TemperaturaMax}")

# Amplitud Términa

for i in range(filas):
    amplitud=matriz_temperaturas[i][1]-matriz_temperaturas[i][0]    
    if mayorAmplitud<=amplitud:
        mayorAmplitud=amplitud
        diaMayorAmplitud=i+1 # Días van del 1 al 7, pero el rango del for va de 0 a 6

print(f"\nLa mayor amplitud térmica fue {mayorAmplitud} y fue registrada el día {diaMayorAmplitud}")

print("\n¡Muchas gracias y hasta luego!")

# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
#   • Mostrar el promedio de cada estudiante.
#   • Mostrar el promedio de cada materia.

print(f"Actividad 8\n")
print("¡Hola!")

matriz_notas=[
    [7, 8, 10], # Estudiante 1
    [6, 9, 9],  # Estudiante 2
    [6, 8, 9],  # Estudiante 3
    [5, 7, 10],  # Estudiante 4
    [8, 6, 9],  # Estudiante 5
]

# Variables a usar
sumaEstudiante=0
sumaMaterias=0
promedioPorMateria=0
promedioEstudiante=0
filas=len(matriz_notas)
columnas=len(matriz_notas[1])

# Promedio de cada estudiante 
print("\nPromedio por estudiante: ")
for i in range(filas):
    sumaEstudiante=0
    sumaEstudiante=sum(matriz_notas[i])   # Sumatoria notas de cada estudiante
    promedioEstudiante=sumaEstudiante/columnas
    print(f"El promedio de notas del estudiante {i+1} es {promedioEstudiante}")
    

# Promedio de cada materia
print("\nPromedio por materia: ")
for j in range(columnas):
    sumaMaterias=0
    for i in range(filas):
        sumaMaterias+=matriz_notas[i][j] # Sumatoria notas por cada Materia
    promedioPorMateria=sumaMaterias/filas
    print(f"El promedio de notas de la materia {j+1} es {promedioPorMateria}")
    

print("\n¡Muchas gracias y hasta luego!")

# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#   • Inicializarlo con guiones "-" representando casillas vacías.
#   • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#   • Mostrar el tablero después de cada jugada.

print(f"Actividad 9\n")
print("¡Hola!")
print("Vamos a jugar al Ta-Te_Ti 😎")

# Tablero del Ta-Te-Ti Inicializado con guiones "-" representando casillas vacías.
tablero=[
    ["-", "-", "-"], 
    ["-", "-", "-"],
    ["-", "-", "-"],
    ]

# Variables a usar
filas=len(tablero)
columnas=len(tablero[1])

# Mostrar tablero
print("\nTablero inicial:")
for i in range(3):
    print(tablero[i][0], tablero[i][1], tablero[i][2])
print()


ganador = None  # Aún no hay ganador

#Juego

while ganador is None:         # Mientras no haya un ganador
    for jugador in ["X", "O"]:                      # Dos turnos para dos jugadores
        print(f"Turno del jugador {jugador} 🤔")
        fila = int(input("Ingrese la fila (0, 1, 2): "))
        while fila not in [0, 1, 2]:               # Validación de fila
            print("\nFila inválida🚷. Intente de nuevo.")
            fila = int(input("Ingrese la fila (0, 1, 2): "))

        columna = int(input("\nIngrese la columna (0, 1, 2): "))
        while columna not in [0, 1, 2]:         # Validación de columna
            print("\nColumna inválida 🚷. Intente de nuevo.")
            columna = int(input("Ingrese la columna (0, 1, 2): "))

        # Esto obliga al jugador a elegir un casillero vacío:

        while tablero[fila][columna] != "-":            
            print("\nCasilla ocupada 😱. Intente de nuevo.")
            fila = int(input("Ingrese la fila (0, 1, 2): "))
            while fila not in [0, 1, 2]:               # Validación de fila
                print("\nFila inválida 🚷. Intente de nuevo.")
                fila = int(input("Ingrese la fila (0, 1, 2): "))

            columna = int(input("Ingrese la columna (0, 1, 2): "))
            while columna not in [0, 1, 2]:         # Validación de columna
                print("\nColumna inválida 🚷. Intente de nuevo.")
                columna = int(input("Ingrese la columna (0, 1, 2): "))        

        tablero[fila][columna] = jugador

        # Detectar si hay ganador

        for i in range(3):    
            if tablero[i][0]==tablero[i][1]==tablero[i][2]!="-":
                ganador=tablero[i][0]
                break
            elif tablero[0][i]==tablero[1][i]==tablero[2][i]!="-":
                ganador=tablero[0][i]
                break
        if tablero[0][0]==tablero[1][1]==tablero[2][2]!="-":
            ganador=tablero[0][0]
            break
        elif tablero[0][2]==tablero[1][1]==tablero[2][0]!="-":
            ganador=tablero[0][2]  
            break

        # Mostrar tablero

        print("\nTablero después de la jugada:")

        for i in range(3):
            print(tablero[i][0], tablero[i][1], tablero[i][2])
        print()

print(f"\n🥳🥳🥳¡Ganó el jugador {ganador}! 🥳🥳🥳")
print("\n¡Muchas gracias y hasta luego!")

