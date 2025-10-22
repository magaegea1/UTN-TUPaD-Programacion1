#Tp 8 - Estructuras de Datos Complejos - TUPaD
print("--- TP 8 - Estructuras de Datos Complejos ---\n")

#-------------------------------------------------------------------------
# Actividad 1. Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt 
# con tres productos. Cada línea debe tener: nombre,precio,cantidad

# Actividad 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea, 
# la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

# Actividad 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad) y 
# lo agregue al archivo sin borrar el contenido existente. 

# Actividad 4. Cargar productos en una lista de diccionarios: Al leer el archivo, 
# cargar los datos en una lista llamada productos, donde cada elemento sea un diccionario con claves: 
# nombre, precio, cantidad. 

# Actividad 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. 
# Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. 
# Si no existe, mostrar un mensaje de error. 

# Actividad 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, 
# sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados 
# desde la lista.


print("_"*40, "\n")
print(f"Actividades \n")
print("¡Hola!\n")

# Actividad 1: Crear el archivo inicial
with open("productos.txt", "w") as archivo:
    archivo.write("nombre,precio,cantidad\n")
    archivo.write("Agua,1000,20\n")
    archivo.write("Chocolate,3500,15\n")
    archivo.write("Alfajor,1700,17\n")

print ("Se ha creado el archivo: productos.txt\n")
    
# Actividad 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea, 
# la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

print("Se mostrarán los productos\n")

with open("productos.txt", "r") as archivo:
    # Saltar la primera línea con los encabezados
    archivo.readline()
    for linea in archivo:
        datos = linea.strip().split(",")
        nombre=datos[0].strip()
        precio=datos[1].strip()
        cantidad=datos[2].strip()
        print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")

# Actividad 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad) y 
# lo agregue al archivo sin borrar el contenido existente.

# Función para validar texto
def validar_texto():
    valido=False
    while not valido:
        texto=input(" ").strip().title()
        if texto=="":
            print("Disculpe, pero no ha ingresado nada, intente nuevamente: ", end="")
        else:
            valido=True
    return texto        
# Función para validar precios
def validar_precio():
    valido=False
    while not valido:
        numero_texto=input(" ").strip()
        try:
            numero=float(numero_texto)
            if numero>0:
                return numero
            else:
                print("Disculpe, pero el precio no puede ser un número negativo ", end="")
        except ValueError:
            print("Disculpe, pero debe ingresar un precio válido mayor a cero: ", end="")

#Función para validar la cantidad
def validar_cantidad():
    valido=False
    while not valido:
        numero_texto=input(" ").strip()
        try:
            numero=int(numero_texto)
            if 0<numero<=1001:
                return numero
            else:
                print("Disculpe, pero debe ingresar un número válido entre 1 y 1000: ", end="")
        except ValueError:
            print("Disculpe, pero no se ha ingresado una cantidad, intente nuevamente: ", end="")

# Solicitar al usuario que agregue un nuevo producto            
print()
agregar_mas=True
while agregar_mas:
    agregar=input("¿Desea agregar un nuevo producto? s/n: ").strip().lower()
    if agregar=="n":
        agregar_mas=False
    elif agregar!="s":
        print("Disculpe, no se a seleccionado una opción válida")
    else:
        with open("productos.txt", "a") as archivo:
            print("\nIngrese el producto que desea agregar: ", end="")
            nombre=validar_texto()
            print(f"\nIngrese el precio de {nombre}: ", end="")
            precio=validar_precio()
            print(f"\nIngrese la cantidad de {nombre} que desea agregar: ", end="")
            cantidad=validar_cantidad()
            archivo.write(f"{nombre},{precio},{cantidad}\n")

# Actividad 4. Cargar productos en una lista de diccionarios: Al leer el archivo, 
# cargar los datos en una lista llamada productos, donde cada elemento sea un diccionario con claves: 
# nombre, precio, cantidad.

lista_productos=[]

with open("productos.txt", "r") as archivo:
    # Saltar la primera línea con los encabezados
    archivo.readline() 

    # Recorrer línea a línea del archivo
    for linea in archivo:

        # Desempaqueto las partes de cada línea
        nombre, precio, cantidad = linea.strip().split(",")

        # Armo una linsta con las partes desempaquetadas
        articulo={
            "nombre": nombre.strip(), 
            "precio": float(precio.strip()), 
            "cantidad": int(cantidad.strip()),   
        }

        # Crear una lista de diccionarios
        lista_productos.append(articulo)

# Actividad 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. 
# Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. 
# Si no existe, mostrar un mensaje de error. 

salir=False
while not salir:
    print("\n¿Qué producto deseas buscar? ", end="")
    nombre_buscado=validar_texto()

    encontrado=False  #Variable de control para poder mostrar al usuario si no se encontró

    # Vamos a recorrer la lista para buscar el producto
    for diccionario in lista_productos:
        if diccionario['nombre']==nombre_buscado: #Ya estaba normalizado con title()
            print("\n¡Producto encontrado!")
            print(f"Producto: {diccionario['nombre']}")
            print(f"Precio: {diccionario['precio']}")
            print(f"Cantidad: {diccionario['cantidad']}")
            encontrado=True
            break #Para que no siga recorriendo la lista si ya lo encontró

    if not encontrado:
        print("Disculpe, no disponemos de ese producto")
            
    continuar_busqueda=input("Si desea buscar otro producto presione 's': ").strip().lower()
    if continuar_busqueda!="s":
        salir=True
            


# Actividad 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, 
# sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados 
# desde la lista.

with open("productos.txt", "w") as archivo:
    # Encabezado
    archivo.write("nombre,precio,cantidad\n")
    for diccionario in lista_productos:
        archivo.write(f"{diccionario['nombre']},{diccionario['precio']},{diccionario['cantidad']}\n")
    
print("\nEl archivo actualizado de productos es:")
with open("productos.txt", "r") as archivo:
    print(archivo.readlines())

print("\n¡Muchas gracias y hasta luego!\n")

