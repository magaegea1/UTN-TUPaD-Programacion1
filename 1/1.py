print("TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN A DISTANCIA ")
print ("Segundo Parcial – Programación 1 \n")

print("Enunciado:\n")
print("La biblioteca escolar necesita modernizar su forma de administrar el catálogo de libros y") 
print("el stock de ejemplares disponibles. Tu tarea es desarrollar una aplicación de consola en Python") 
print("que permita cargar, consultar y actualizar el inventario de manera sencilla, manteniendo registros") 
print("persistentes en un archivo CSV.\n")

print ("-"*40)
print ("\nBiblioteca Escolar Modernizada\n")
print ("-"*40)

# Importar módulos:
import csv  # Para trabajar con archivos CSV de forma segura y estructurada
import os   # Para verificar si el archivo existe sin usar excepciones (que están prohibidas en el parcial)


NOMBRE_ARCHIVO = "catalogo.csv"
print("Archivo de trabajo:", NOMBRE_ARCHIVO)

# *** Funciones que trabajan directamente con el archivo csv ***

# Función para cargar el catálogo desde el archivo csv
def obtener_catalogo_desde_csv():
    """
    Carga el catálogo de libros desde el archivo CSV y lo transforma en una lista de diccionarios.

    Si el archivo 'catalogo.csv' no existe, lo crea con el encabezado correspondiente y devuelve una lista vacía.

    Cada fila del archivo se convierte en un diccionario con las claves:
    - 'TITULO': texto normalizado (sin espacios extremos, con mayúscula inicial en cada palabra)
    - 'CANTIDAD': número entero de ejemplares disponibles

    Devuelve:
    - Una lista de diccionarios que representa el catálogo actual de la biblioteca.
    """

    catalogo_lista = []
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["TITULO", "CANTIDAD"])
            escritor.writeheader()
        print("Archivo creado con encabezado.")
        return catalogo_lista

    # Lectura del archivo existente
    with open(NOMBRE_ARCHIVO, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            catalogo_lista.append({
                "TITULO": fila["TITULO"].strip().title(),
                "CANTIDAD": int(fila["CANTIDAD"].strip())
            })
    return catalogo_lista

# Función para actualizar el archivo catalogo.csv desde la lista de diccionarios sobreescribiendo 
# todo cada vez que se modifica el inventario

# Se decidió que no hayan más formas de escribir en el catálogo csv (por ejemplo, agregando con "a") porque
# se le da prioridad a la seguridad del archivo csv
# De este modo sólo se cambia el archivo csv sobreescribiendo cuando se termina cada caso del menú en el 
# que se modifique la lista de diccionarios, esta es la forma en que se actualizará el archivo csv cada vez
# que se modifique el inventario. Esto es bueno para la seguridad del archivo csv, aunque si
# el archivo llegara a ser demasiado largo no sería tan bueno en cuanto al uso de los recursos
def guardar_catalogo_en_csv(catalogo_lista):
    """
    Sobrescribe el archivo 'catalogo.csv' en base a la lista de diccionarios actualizada.

    Parámetros:
    - catalogo_lista: lista de diccionarios en memoria, donde cada diccionario representa un libro
      con las claves 'TITULO' (str) y 'CANTIDAD' (int)

    Esta función se llama al finalizar cada operación del menú que modifica el inventario.
    Prioriza la seguridad del archivo CSV evitando escrituras parciales o inconsistentes,
    y garantiza que el archivo refleje fielmente el estado actual del catálogo en memoria.
    """
    with open(NOMBRE_ARCHIVO, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["TITULO", "CANTIDAD"])
        escritor.writeheader()
        for libro in catalogo_lista:
            escritor.writerow({
                "TITULO": libro["TITULO"],
                "CANTIDAD": libro["CANTIDAD"]
            })
    return "El archivo catalogo.csv ha sido actualizado correctamente"


# *** Validaciones: ***

# Función para validar que se ingrese una cadena de texto que no esté vacía, limpiar y normalizar con title.
def validar_texto_vacio_y_normalizar():
    """
    validar_texto_vacio_y_normalizar() es una función que se ocupa de revisar que el texto ingresado por el usuario:
    - No esté vacío
    - Limpia los extremos para que no haya espacios ni saltos
    - Elimina espacios extra que hayan internamente
    - Lo normaliza usando title() para que la primera letra de cada palabra sea mayúscula (se usará en títulos)
    Esta función no recibe parámetros. Se llama cuando se espera que el usuario ingrese una cadena de texto 
    por teclado.
    Devuelve el texto validado y normalizado para ser usado como título en el catálogo.
    """
    valido = False    
    while not valido:
        texto = " ".join(input("").strip().split()).title()
        if texto == "":
            print("\tDisculpe, pero no ha ingresado ningún título, intente nuevamente: ", end="")
        else:
            return texto

# Función para validar si el título ingresado está o no dentro de la lista de diccionarios
def validar_titulo_ya_existe(catalogo_lista, nuevo_titulo):
    """
    Verifica si el título ingresado ya existe en el catálogo en memoria.

    Recorre la lista de diccionarios 'catalogo_lista' y compara los títulos normalizados
    para evitar duplicaciones. La comparación es insensible a mayúsculas y espacios redundantes.

    Parámetros:
    - catalogo_lista: lista de diccionarios con los libros y sus cantidades disponibles
    - nuevo_titulo: texto ingresado por el usuario, ya validado y normalizado

    Devuelve:
    - True si el título ya existe
    - False si es un título nuevo
    """
    for libro in catalogo_lista:
        if libro["TITULO"].strip().title() == nuevo_titulo:
            return True
    return False


# Función para validar que se ingrese una cantidad válida como entero positivo con un máximo de 100 (de 1 a 100).
def validar_entero_positivo_hasta_100():
    """
    validar_entero_positivo_hasta_100() es una función que se ocupa de revisar que el texto ingresado por el usuario:
    - No esté vacío
    - Elimina espacios extremos e internos
    - Verifica que sean solo números
    - Convierte a entero
    - Valida que esté entre 1 y 100 inclusive

    Devuelve el número entero validado para ser usado como cantidad de libros.
    """
    valido = False    
    while not valido:
        cantidad = " ".join(input("").strip().split())
        
        if not cantidad.isdigit():
            print("\tDisculpe, debe ingresar un número entero entre 1 y 100. Intente nuevamente: ", end="")
        else:
            numero = int(cantidad)
            if 1 <= numero <= 100:
                return numero
            else:
                print("\tEl número debe estar entre 1 y 100. Intente nuevamente: ", end="")




# *** Opciones del Menú: ***


# 1. Función: Ingresar títulos (múltiples): permite cargar varios libros de una vez.
#             Permite ingresar varios libros en una misma sesión hasta que el usuario decida salir


def ingresar_titulos_multiples(catalogo_lista):
    """
    Permite ingresar múltiples libros al catálogo en memoria en una sola operación.

    Por cada libro, solicita al usuario:
    - TÍTULO: validado para que no esté vacío ni duplicado
    - CANTIDAD: validada como entero entre 1 y 100

    Utiliza funciones de validación previamente desarrolladas para asegurar la consistencia de los datos.
    Cada nuevo libro se agrega a la lista de diccionarios 'catalogo_lista', y al finalizar se actualiza el archivo CSV.

    Parámetros:
    - catalogo_lista: lista de diccionarios con los libros y sus cantidades disponibles

    Devuelve:
    - No devuelve valores explícitos.
    - Actualiza la lista 'catalogo_lista' en memoria y el archivo 'catalogo.csv' 
      mediante la función guardar_catalogo_en_csv().
    """

    print("\n1. Ingresar títulos (múltiples): permite cargar varios libros de una vez.")            
    print("\tPor cada libro, debe indicar:")
    print("\t\t- El Título (tenga cuidado de que no esté vacío ni duplicado)")
    print("\t\t- La Cantidad: entre 0 y 100")
    
    #Lista para armar el lote de libros
    lote_titulos=[]

    #Bucle para agregar varios libros hasta que el usuario decida salir
    salir = False
    while not salir:
        print(f"\n\tPor favor, indique cuántos libros quiere cargar: ",end="")
        cantidad_de_titulos=validar_entero_positivo_hasta_100()
        for i in range(1, cantidad_de_titulos+1):
            print(f"\n\tPor favor, indique el título {i} del libro que desea cargar: ", end="")
            titulo_nuevo=validar_texto_vacio_y_normalizar()
            if validar_titulo_ya_existe(catalogo_lista, titulo_nuevo):
                print("\tDisculpe, pero ese título ya existe en el inventario")
            else:
                lote_titulos.append(titulo_nuevo)

        for libro in lote_titulos:
            print(f"\n\tPor favor, indique la cantidad de libros de {libro} que quiere cargar: ", end="")
            cantidad=validar_entero_positivo_hasta_100()
            catalogo_lista.append({
                "TITULO": libro,
                "CANTIDAD": cantidad
            })
            print(f"\tDel libro: {libro} se han agregado {cantidad} ejemplares")

        print(f"\n\t✅ {guardar_catalogo_en_csv(catalogo_lista)}")
        
        # Limpieza del lote para la próxima ronda
        lote_titulos.clear()

        quiere_salir = input("\n\tSi desea salir al menú principal presione 's': ").strip().lower()
        if quiere_salir=="s":
            print("\tVolvemos al menú principal")
            return
        else:
            print("\tContinuamos cargando más libros...")


# 2. Función: Ingresar ejemplares: sumar una cantidad a un título existente
def ingresar_ejemplares(catalogo_lista):
    """
    Permite agregar ejemplares a un título ya existente en el catálogo en memoria.

    Solicita al usuario:
    - TÍTULO: validado para que exista en el catálogo
    - CANTIDAD: validada como entero entre 1 y 100

    Si el título existe, se incrementa la cantidad disponible en el catálogo.
    Utiliza funciones de validación previamente desarrolladas para asegurar la consistencia de los datos.
    Al finalizar, se actualiza el archivo 'catalogo.csv' para reflejar los cambios.

    Parámetros:
    - catalogo_lista: lista de diccionarios con los libros y sus cantidades disponibles

    Devuelve:
    - No devuelve valores explícitos.
    - Actualiza la lista 'catalogo_lista' en memoria y el archivo 'catalogo.csv' 
      mediante la función guardar_catalogo_en_csv().
    """

    print("\n2. Ingresar ejemplares: sumar una cantidad a un título existente")            
    print("\tPor cada libro, debe indicar:")
    print("\t\t- El Título (tenga cuidado de que no esté vacío)")
    print("\t\t- La Cantidad: entre 1 y 100")
    
    #Bucle para agregar ejemplares a un libro ya existente
    salir = False
    while not salir:
        print("\n\tPor favor, indique el título del libro que desea cargar: ", end="")
        titulo_existente = validar_texto_vacio_y_normalizar()
        if not validar_titulo_ya_existe(catalogo_lista, titulo_existente):
            print(f"\tDisculpe, pero ese {titulo_existente} no existe en el inventario")
            print("\tSi desea agregarlo debe hacerlo desde la opción 1 del menú principal")
            quiere_salir = input("\tSi desea salir al menú principal presione 's': ").strip().lower()
            if quiere_salir=="s":
                print("\tVolvemos al menú principal")
                return
        else:
            while True:
                print(f"\n\tPor favor, indique la cantidad de libros de {titulo_existente} que quiere cargar: ", end="")
                cantidad=validar_entero_positivo_hasta_100()
                if cantidad==0:
                    print("\tDisculpe, pero no se puede agregar 0 ejemplares")
                    quiere_salir = input("\tSi desea salir al menú principal presione 's': ").strip().lower()
                    if quiere_salir=="s":
                        print("\tVolvemos al menú principal")
                        return
                else:
                    break
            
            for libro in catalogo_lista:
                if libro["TITULO"].strip().title()==titulo_existente:
                    libro["CANTIDAD"]+=cantidad
                    break

            print(f"\n\t✅ {guardar_catalogo_en_csv(catalogo_lista)}")
            print(f"\tDel libro: {titulo_existente} se han agregado {cantidad} ejemplares")
            quiere_salir = input("\n\tSi desea salir al menú principal presione 's': ").strip().lower()
            if quiere_salir=="s":
                print("\tVolvemos al menú principal")
                return
            else:
                print("\tContinuamos cargando más ejemplares...")





# 3. Función: Mostrar catálogo: listar todos los libros con su stock actual
def mostrar_catalogo(catalogo_lista):
    """
    Muestra todos los libros del catálogo con su cantidad disponible.
    """
    print("\nCatálogo actual:")
    if not catalogo_lista:
        print("\tEl catálogo está vacío.")
        return

    for libro in sorted(catalogo_lista):
        titulo = libro["TITULO"]
        cantidad = libro["CANTIDAD"]
        print(f"\t- {titulo}: {cantidad} ejemplares")


# 4. Función: Consultar disponibilidad: buscar un título y mostrar cuántos ejemplares hay disponibles
def consultar_disponibilidad(catalogo_lista):
    """
    Buscar un título y mostrar cuántos ejemplares hay disponibles
    """
    print("\n\tDisponibilidad:")
    if not catalogo_lista:
        print("\tEl catálogo está vacío.")
        return

    #Bucle para buscar libros y mostrar cuántos ejemplares hay del mismo
    salir = False
    while not salir:
        print("\n\tPor favor, indique el título del libro que desea buscar: ", end="")
        consulta=validar_texto_vacio_y_normalizar()
        if validar_titulo_ya_existe(catalogo_lista, consulta):
            for libro in catalogo_lista:
                if libro["TITULO"] == consulta:
                    print(f"\t- {consulta}: {libro['CANTIDAD']} ejemplares")
                    break
        else:
            print("\tDisculpe, pero ese libro no está en el inventario")
        
        quiere_salir = input("\tSi desea salir al menú principal presione 's': ").strip().lower()
        if quiere_salir=="s":
                print("\tVolvemos al menú principal")
                return


# 5. Función: Listar agotados: mostrar solo los títulos que están agotados
def listar_agotados(catalogo_lista):
    """
    Buscar los títulos que están agotados y mostrarlos por pantalla
    """
    print("\n\tLibros Agotados:")
    if not catalogo_lista:
        print("\tEl catálogo está vacío.")
        return

    #Bucle para buscar libros agotados y mostrarlos en pantalla
    contador=0
    for libro in sorted(catalogo_lista):
        if libro["CANTIDAD"] == 0:
            print(f"\t- {libro['TITULO']}: {libro['CANTIDAD']} ejemplares")
            contador+=1
    if contador==0:
        print("\tNo hay libros agotados")    
    print("\tVolvemos al menú principal")
    return

# 6. Función: Agregar título: alta de un libro individual con su cantidad inicial
def ingresar_titulos_individualmente(catalogo_lista):
    """
    Permite ingresar libros uno a uno al catálogo en memoria.

    Por cada libro, solicita al usuario:
    - TÍTULO: validado para que no esté vacío ni duplicado
    - CANTIDAD: validada como entero entre 0 y 100

    Utiliza funciones de validación previamente desarrolladas para asegurar la consistencia de los datos.
    Cada nuevo libro se agrega a la lista de diccionarios 'catalogo_lista', y al finalizar se actualiza el archivo CSV.

    Parámetros:
    - catalogo_lista: lista de diccionarios con los libros y sus cantidades disponibles

    Devuelve:
    - No devuelve valores explícitos.
    - Actualiza la lista 'catalogo_lista' en memoria y el archivo 'catalogo.csv' 
      mediante la función guardar_catalogo_en_csv().
    """

    print("\n6. Ingresar título: permite cargar un sólo libro con su cantidad de ejemplares.")            
    print("\tDebe indicar:")
    print("\t\t- El Título (tenga cuidado de que no esté vacío ni duplicado)")
    print("\t\t- La Cantidad: entre 1 y 100")
    
    #Bucle para agregar libros, uno por uno, hasta que el usuario decida salir
    salir = False
    while not salir:
        print("\n\tPor favor, indique el título del libro que desea cargar: ", end="")
        titulo_nuevo=validar_texto_vacio_y_normalizar()
        if validar_titulo_ya_existe(catalogo_lista, titulo_nuevo):
            print("\tDisculpe, pero ese título ya existe en el inventario")
            quiere_salir = input("\tSi desea salir al menú principal presione 's': ").strip().lower()
            if quiere_salir=="s":
                print("\tVolvemos al menú principal")
                return
        else:
            print(f"\n\tPor favor, indique la cantidad de libros de {titulo_nuevo} que quiere cargar: ", end="")
            cantidad=validar_entero_positivo_hasta_100()
            catalogo_lista.append({
                "TITULO": titulo_nuevo,
                "CANTIDAD": cantidad
            })
            print(f"\n\t✅ {guardar_catalogo_en_csv(catalogo_lista)}")
            print(f"\tDel libro: {titulo_nuevo} se han agregado {cantidad} ejemplares")
            quiere_salir = input("\n\tSi desea salir al menú principal presione 's': ").strip().lower()
            if quiere_salir=="s":
                print("\tVolvemos al menú principal")
                return
            else:
                print("\tContinuamos cargando más libros...")

# 7. Función: Actualizar ejemplares (préstamo/devolución)




def mostrar_menu():
    # Opciones del menú
    print ("-"*40)
    print("1. Ingresar títulos (múltiples): permite cargar varios libros de una vez.") 
    print("2. Ingresar ejemplares: sumar una cantidad a un título existente.")
    print("3. Mostrar catálogo: listar todos los libros con su stock actual.")
    print("4. Consultar disponibilidad: buscar un título y mostrar cuántos ejemplares hay disponibles.")
    print("5. Listar agotados: mostrar solo los títulos que están agotados.")
    print("6. Agregar título: alta de un libro individual con su cantidad inicial.")
    print("7. Actualizar ejemplares (préstamo/devolución):")
    print("8. Salir: finalizar la aplicación.")
    print ("-"*40)

def pedir_opcion():
    valido=False
    while not valido:
        opcion = input("Por favor, ingrese la opción deseada: ").strip()
        if opcion.isdigit() and 0<int(opcion)<9:
            valido=True
        else:
            print("Disculpe, pero la opción ingresada no es válida, intente nuevamente...")
    return int(opcion)



def menu_principal(catalogo_lista):
    while True:
        mostrar_menu()
        # Interacción con el usuario para que ingrese la opción que desea
        num_opcion=pedir_opcion()

        match num_opcion: 
            case 1:
                ingresar_titulos_multiples(catalogo_lista)
                
            case 2:
                ingresar_ejemplares(catalogo_lista)
                
            case 3:
                mostrar_catalogo(catalogo_lista)

            case 4:
                consultar_disponibilidad(catalogo_lista)
                
            case 5:
                listar_agotados(catalogo_lista)

            case 6:
                ingresar_titulos_individualmente(catalogo_lista)
            case 7:
                # Préstamo: restar 1 solo si CANTIDAD > 0.
                # Devolución: sumar 1.
                #actualizar_ejemplares_1(catalogo)
                pass # Luego lo completo
            case 8:
                print("¡Gracias por usar el sistema! \n¡Hasta Pronto!")
                break

catalogo_lista=obtener_catalogo_desde_csv()
menu_principal(catalogo_lista)







      

