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

def obtener_catalogo_desde_csv():
    catalogo = []
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["TITULO", "CANTIDAD"])
            escritor.writeheader()
        print("🌱 Archivo creado con encabezado.")
        return catalogo

    # Lectura del archivo existente
    with open(NOMBRE_ARCHIVO, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            catalogo.append({
                "TITULO": fila["TITULO"].strip().title(),
                "CANTIDAD": int(fila["CANTIDAD"].strip())
            })
    return catalogo

# Para actualizar el archivo catalogo.csv
def guardar_catalogo_en_csv(catalogo):
    with open(NOMBRE_ARCHIVO, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["TITULO", "CANTIDAD"])
        escritor.writeheader()
        for libro in catalogo:
            escritor.writerow({
                "TITULO": libro["TITULO"],
                "CANTIDAD": libro["CANTIDAD"]
            })




def validar_texto():
     valido=False    
     while not valido:
        texto=input("").strip().title()
        if texto=="":
           print("Disculpe, pero no ha ingresado ningún título, intente nuevamente...")
        else:
            return texto

def validar_datos_libro(titulo, cantidad):


# 1. Función: Ingresar títulos (múltiples): permite cargar varios libros de una vez.
def ingresar_titulos_multiples(catalogo):
    print("1. Ingresar títulos (múltiples): permite cargar varios libros de una vez.")            
    print("\tPor favor, indique la cantidad de libros que quiere cargar")
    print("\tPor cada libro, debe indicar:")
    print("\t\t- El Título (tenga cuidado de que no esté vacío ni duplicado)")
    print("\t\t- La Cantidad (a partir de 0 'cero')")


    
# 2. Función: Ingresar ejemplares: sumar una cantidad a un título existente





# 3. Función: Mostrar catálogo: listar todos los libros con su stock actual
def mostrar_catalogo(catalogo):
    print("--- Catálogo Completo ---")    
    inventario=obtener_catalogo_desde_csv()
    print(inventario)

# 4. Función: Consultar disponibilidad: buscar un título y mostrar cuántos ejemplares hay disponibles

# 5. Función: Listar agotados: mostrar solo los títulos que están agotados

# 6. Función: Agregar título: alta de un libro individual con su cantidad inicial

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



def menu_principal(catalogo):
    while True:
        mostrar_menu()
        # Interacción con el usuario para que ingrese la opción que desea
        num_opcion=pedir_opcion()

        match num_opcion: 
            case 1:
                #ingresar_titulos_multiples(catalogo)
                pass # Luego lo completo
            case 2:
                #ingresar_ejemplares(catalogo)
                pass # Luego lo completo
            case 3:
                #mostrar_catalogo(catalogo)
                pass # Luego lo completo
            case 4:
                #consultar_disponibilidad(catalogo)
                pass # Luego lo completo
            case 5:
                #listar_agotados(catalogo)
                pass # Luego lo completo
            case 6:
                #agregar_un_título(catalogo)
                pass # Luego lo completo
            case 7:
                # Préstamo: restar 1 solo si CANTIDAD > 0.
                # Devolución: sumar 1.
                #actualizar_ejemplares_1(catalogo)
                pass # Luego lo completo
            case 8:
                print("¡Gracias por usar el sistema! \n¡Hasta Pronto!")
                break

catalogo = obtener_catalogo()
menu_principal(catalogo)







      

