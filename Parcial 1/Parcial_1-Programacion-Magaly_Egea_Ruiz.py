print("TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN A DISTANCIA ")
print ("Primer Parcial – Programación 1 \n")

print ("Enunciado: \nLa biblioteca escolar necesita un sistema de gestión sencillo para su catálogo de libros y las") 
print ("copias disponibles. Se pide desarrollar un programa con una interfaz basada en menú que")
print ("utilice listas paralelas (una para titulos[] y otra para ejemplares[]). Cada título debe estar")
print ("vinculado a su número correspondiente de copias utilizando el mismo índice en ambas listas.")
print ("Se debe utilizar un bucle while para navegar por las opciones del menú hasta que el usuario elija salir.")
print ("----------------------")

print ("\nBiblioteca Escolar\n")

# Definir las listas
titulos=[]
ejemplares=[]
opcion_menu=0
correcto=""
titulo=""


print("¡Hola! \n    \n    📚 🏫 Bienvenido/a a la Biblioteca de la Escuela 🏫 📚") 

while opcion_menu!="8":    # Inicio del menú de opciones con sus acciones
    # Mostrar al usuario las opciones disponibles del menú
    print("\nElige el número de la opción deseada\n" \
    "1) 📖 Ingresar títulos: ¿Qué libro deseas agregar?\n" \
    "2) 🔢 Ingresar ejemplares: ¿Cuántas copias del libro querés agregar?\n" \
    "3) 📂 Mostrar catálogo: ¿Querés ver el catálogo completo de libros y ejemplares disponibles?\n" \
    "4) 🔍 Consultar disponibilidad: ¿Querés saber cuántos ejemplares hay de un título específico?\n" \
    "5) ❌ Listar agotados: ¿Querés saber cuáles libros están agotados?\n" \
    "6) 📥 Agregar título + ejemplares: ¿Te gustaría incorporar un nuevo libro y elegir cuántas copias agregar?\n" \
    "7) ✍️  Actualizar ejemplares (préstamo/devolución): ¿Hay algún préstamo o devolución que registrar?\n" \
    "8) 🛎️  Salir: Si ya terminaste y deseas salir\n")

    opcion_menu=input("¿Cuál es el número de la opción que deseas? ") # El usuario ingresa su elección
    opcion_menu=opcion_menu.strip()   # Para eliminar espacios que se hayan ingresado por error

    match opcion_menu:
        case "1":
            print("\nHas seleccionado la opción 1: 📖 Ingresar títulos") 
            
            continuar_agregando = True
            while continuar_agregando:

                correcto = ""          
                while correcto != "s":

                    titulo_nuevo = input("\n¿Qué libro deseas agregar?: ").strip().title()

                    while not titulo_nuevo:
                        print("El título no puede estar vacío. Intentá nuevamente")   # Validar que el título no esté vacío
                        titulo_nuevo = input("\n¿Qué libro deseas agregar?: ").strip().title()

                    # Permitir al usario revisar lo que escribió antes de guadarlo    
                    print(f"\nHas ingresado el libro: '{titulo_nuevo}' ¿Está bien?")
                    correcto = input("Si es correcto, ingresá 's'; de lo contrario, cualquier otra letra: ").strip().lower()

                    if correcto == "s":
                        print("\nConfirmado\n")

                    else:
                        print("\nIngresa nuevamente el libro")
                    
                if titulo_nuevo in titulos:
                    # Validar si el libro ya existía en la lista
                    print(f"El título '{titulo_nuevo}' ya existe en el catálogo. Podés agregar ejemplares si lo deseás.")
                else:
                    titulos.append(titulo_nuevo)     # Agregar libro nuevo a la lista de titulos
                    indice = titulos.index(titulo_nuevo)

                    # Agregar la cantidad inicial    
                    cantidad_ejemplares = input(f"¿Cuántos ejemplares iniciales del libro '{titulo_nuevo}' querés registrar?: ").strip()
                    while not cantidad_ejemplares.isdigit():
                        print("\nNo se ha ingresado un número válido. Intentá nuevamente\n")
                        cantidad_ejemplares = input("¿Cuántos ejemplares iniciales del libro querés registrar?: ").strip()

                    cantidad_ejemplares = int(cantidad_ejemplares)
                    ejemplares.insert(indice, cantidad_ejemplares)

                    print(f"\nSe ha agregado el libro: '{titulos[indice]}' con {ejemplares[indice]} ejemplares al catálogo adecuadamente")

                print("\n¿Deseas agregar más libros al catálogo?")    
                seguir = input("('s' para agregar más libros, de lo contrario presiona cualquier tecla): ").strip().lower()
                if seguir != "s":
                    continuar_agregando = False
                    input("\nVolvemos al menú principal 📚 🏫\nPresioná Enter para continuar...")

        case "2":
            print("\nHas seleccionado la opción 2: 🔢 Ingresar ejemplares:")

            continuar_agregando=True          # Para poder seguir agregando ejemplares antes de salir

            if not titulos:
                print("\nEl catálogo está vacío. No hay libros disponibles para actualizar ejemplares.")
                print("Podés agregar títulos desde el menú principal")
                input("\nPresioná Enter para volver al menú principal 📚 🏫")
                continuar_agregando=False          # Para salir
    
    
            while continuar_agregando:

                titulo=input("\n¿Cuál es el libro al que querés agregar ejemplares?: ").title() 
                # Validar que no esté vacío
                while not titulo:
                    print("El título no puede estar vacío. Intentá nuevamente")
                    titulo = input("\n¿Qué libro deseas agregar?: ").strip().title()

                if titulo in titulos:
                    cantidad_ejemplares=input("¿Cuántas copias del libro querés agregar?: ").strip() # Pedir el título
                    while not cantidad_ejemplares.isdigit():                # Validar que se haya ingresado un número para los ejemplares
                        print("\nNo se ha ingresado un número válido. Intentá nuevamente\n")
                        cantidad_ejemplares=input("¿Cuántas copias del libro querés agregar?: ").strip()
    
                    cantidad_ejemplares=int(cantidad_ejemplares) # Convertir la variable en entero

                    indice=titulos.index(titulo)    # Averiguar el índice correcto del nuevo título para evitar errores
                    print(f"\nSe van a agregar {cantidad_ejemplares} ejemplares al libro {titulo}")
                    ejemplares[indice] += cantidad_ejemplares           # Agregar los ejemplares al título elegido
                    print(f"Ahora hay {ejemplares[indice]} ejemplares del libro {titulo}, se han agregado los ejemplares adecuadamente")
                    
                else:
                    print("\nEse título no existe en el catálogo")
                    print("Podés agregarlo desde la opción 1 si querés agregarlo al catálogo")
    
                print("\n¿Deseas agregar más ejemplares a algún libro?")    
                seguir=input("('s' para agregar más ejemplares, de lo contrario presiona cualquier tecla): ").strip().lower()
                if seguir!="s":
                    continuar_agregando=False
            input("\nVolvemos al menú principal 📚 🏫\n Presioná Enter para continuar...")
           
        case "3":
            print("\nHas seleccionado la opción 3: 📂 Mostrar catálogo") 
            print("\nCatálogo actual de la Biblioteca")

            if not titulos:           # Verificamos que haya libros en el catálogo
                print("No hay ningún libro en el catálogo aún")
                print("Podés agregarlo desde la opción 1 si querés agregarlo al catálogo")
            
            else:
                for i in range(len(titulos)):            # Recorremos las dos listas de manera paralela con los índices correctos
                    print(f"{titulos[i]}: {ejemplares[i]} ejemplares")
            
            input("\nVolvemos al menú principal 📚 🏫\n Presioná Enter para continuar...")


        case "4":
            print("\nHas seleccionado la opción 4: 🔍 Consultar disponibilidad") 

            continuar_agregando=True          # Para poder seguir agregando libros antes de salir
            while continuar_agregando:

                if not titulos:
                    print("\nEl catálogo está vacío. No hay libros disponibles para consultar.")
                    print("Podés agregarlo al catálogo desde las opciones disponibles en el menú principal")
                    continuar_agregando=False
                    
                else:
                    titulo=input("\n¿Cuál es el libro del que querés consultar la disponibilidad de ejemplares?: ").title() 
                    # Validar que no esté vacío
                    while not titulo:
                        print("El título no puede estar vacío. Intentá nuevamente")
                        titulo = input("\n¿Qué libro deseas consultar?: ").strip().title()

                    if titulo in titulos:
                        indice=titulos.index(titulo)    # Averiguar el índice correcto del nuevo título para evitar errores
                        print(f"\nDel libro '{titulo}' hay {ejemplares[indice]} ejemplares") 
                    else:
                        print("\nEse título no existe en el catálogo")
                        print("Podés agregarlo al catálogo desde el menú principal")

                    print("\n¿Deseas consultar la disponibilidad de algún libro más?")    
                    seguir=input("('s' para consultar, de lo contrario presiona cualquier tecla): ").strip().lower()
                    if seguir!="s":
                        continuar_agregando=False
            input("\nVolvemos al menú principal 📚 🏫\n Presioná Enter para continuar...")


        case "5":
            print("\nHas seleccionado la opción 5: ❌ Listar agotados:\n")

            if not titulos:           # Verificamos que hay títulos en el catálogo
                print("No hay ningún libro en el catálogo aún")
                print("Podés agregarlo desde el menú principal")

            agotados=False
            for i in range(len(ejemplares)):
                if ejemplares[i]==0:
                    print(f"{titulos[i]} = {ejemplares[i]}") # Muestra la lista de libros agotados
                    agotados=True
            if not agotados:
                print("En el catálogo no hay ningún libro agotado")

            input("\nVolvemos al menú principal 📚 🏫\n Presioná Enter para continuar...")


        case "6": 
            print("\nHas seleccionado la opción 6: 📥 Agregar título + ejemplares:")

            continuar_agregando=True          # Para poder seguir agregando libros antes de salir
            while continuar_agregando:

                correcto=""          # Reiniciar la variable cada vez que entra
                while correcto!="s":

                    # Pedir al usuario el título para agregar
                    titulo_nuevo = input("\n¿Qué libro deseas agregar?: ").strip().title()   
                    while not titulo_nuevo:
                        print("El título no puede estar vacío. Intentá nuevamente")   # Validar que el título no esté vacío
                        titulo_nuevo = input("\n¿Qué libro deseas agregar?: ").strip().title()   # Pedir al usuario el título para agregar

                    print(f"\nHas ingresado el libro: '{titulo_nuevo}' ¿Está bien?" ) # Verificar que el usuario escribió bien el libro
                    correcto=input("Si es correcto, ingresá 's'; de lo contrario, cualquier otra letra: " ).strip().lower()
                    if correcto=="s":
                        print("\nConfirmado\n")
                    else:
                        print("\nIngresa nuevamente el libro\n")

                if titulo_nuevo not in titulos:
                    titulos.append(titulo_nuevo)     # Agregar libro nuevo a la lista de titulos
                    indice=titulos.index(titulo_nuevo)    # Averiguar el índice correcto del nuevo título para evitar errores
                                
                    print(f"\nSe ha agregado el libro: '{titulos[indice]}' al catálogo adecuadamente")

                    ejemplares.insert(indice,0)    # Se utiliza para que ambas listas estén indexadas adecuadamente y para poder en la siguiente 
                                                                # parte, agregar más libros si ya ese libro existían previamente
                else:
                    print(f"\nEl título '{titulo_nuevo}' ya existe en el catálogo.")  # Validar si el libro ya existía en la lista
                    print(f"Podés agregar más ejemplares si lo deseás.")

                

                cantidad_ejemplares=input(f"¿Cuántas copias del libro: {titulo_nuevo}, querés agregar?: ").strip() # Pedir el título
                while not cantidad_ejemplares.isdigit():                # Validar que se haya ingresado un número para los ejemplares
                    print("\nNo se ha ingresado un número válido. Intentá nuevamente\n")
                    cantidad_ejemplares=input("¿Cuántas copias del libro querés agregar?: ").strip()
    
                cantidad_ejemplares=int(cantidad_ejemplares) # Convertir la variable en entero
                indice = titulos.index(titulo_nuevo)        # Para mantener ambas listas paralelas

                print(f"\nSe van a agregar {cantidad_ejemplares} ejemplares al libro {titulo_nuevo}")
                ejemplares[indice] += cantidad_ejemplares    # Para agregar ejemplares sin importar si el libro existía antes o no en el catálogo

                print(f"\nAhora hay {ejemplares[indice]} ejemplares del libro {titulos[indice]} \nSe ha agregado todo adecuadamente")
                    
                print("\n¿Deseas agregar más libros al catálogo?")    
                seguir=input("('s' para agregar más libros, de lo contrario presiona cualquier tecla): ").strip().lower()
                if seguir!="s":
                    continuar_agregando=False
            
            input("\nVolvemos al menú principal 📚 🏫\n Presioná Enter para continuar...")

        case "7":

            print("\nHas seleccionado la opción 7: ✍️  Actualizar ejemplares (préstamo/devolución):")

            continuar_agregando = True

            if not titulos:             # Validar que el catálogo no esté vacío
                print("\nEl catálogo está vacío. No hay libros disponibles para actualizar ejemplares.")
                print("Podés agregar títulos desde el menú principal")
                input("\nPresioná Enter para volver al menú principal 📚 🏫")
                continuar_agregando = False

            while continuar_agregando:
        
                titulo = input("\n¿Qué libro deseas actualizar?: ").strip().title()   # Pedir al usuario el título para actualizar
                while not titulo:
                    print("El título no puede estar vacío. Intentá nuevamente")   # Validar que el título no esté vacío
                    titulo = input("\n¿Qué libro deseas actualizar?: ").strip().title()                
                                
                if titulo in titulos:
                
                    indice=titulos.index(titulo)        # Buscar el índice que vincula las dos listas

                    valido = False
                    while not valido:
                        print("\n¿Deseas registrar un préstamo o una devolución?")      # Pedir al usuario si quiere realizar un préstamo o devolución
                        actualizar = input("Ingresa 'p' para préstamos o 'd' para devoluciones: ").strip().lower()
    
                        if actualizar == "d":         # Hacer las devoluciones de a un ejemplar y actualizar
                            print(f"\nSe va a devolver un ejemplar del libro '{titulo}'")
                            ejemplares[indice] += 1
                            print(f"Ahora hay {ejemplares[indice]} ejemplares del libro '{titulos[indice]}'")
                            valido = True

                        elif actualizar == "p":        # Hacer los préstamos de a un ejemplar y actualizar
                            if ejemplares[indice] >= 1:   # Validar que hayan suficientes títulos para prestar
                                print(f"\nSe va a retirar 1 ejemplar del libro '{titulo}' por préstamo")
                                ejemplares[indice] -= 1
                                print(f"Ahora hay {ejemplares[indice]} ejemplares del libro '{titulo}'")
                                valido = True
                            else:              # Avisar al usuario que no hay suficientes títulos para prestar
                                print(f"\nLo siento, no hay suficientes ejemplares de '{titulo}'")
                                print(f"Actualmente hay {ejemplares[indice]} ejemplares disponibles")
                                valido = True

                        else:    # Validar que haya ingresado "d" o "p"
                            print("\nNo se ha ingresado una opción válida. Intentá nuevamente\n") 

                else:   # Validar que el título se encuentre en el catálogo
                    print(f"\nEl libro '{titulo}' no se encuentra en el catálogo. Verificá el nombre o agregalo desde la opción 1\n")

                print("\n¿Deseas realizar más devoluciones o préstamos de algún libro?") # Dar la opción de continuar haciendo más actualizaciones
                seguir = input("('s' para continuar, de lo contrario presiona cualquier tecla para salir al menú principal): ").strip().lower()
                if seguir != "s":
                    continuar_agregando = False
            input("\nVolvemos al menú principal 📚 🏫\nPresioná Enter para continuar...")
        case "8":
            print("👋¡Gracias y Hasta pronto!")
        
        case _:
            print("\nDisculpa, pero la opción ingresada no es válida \nInténtalo nuevamente\n")

            input("\nVolvemos al menú principal 📚 🏫\n Presioná Enter para continuar...")