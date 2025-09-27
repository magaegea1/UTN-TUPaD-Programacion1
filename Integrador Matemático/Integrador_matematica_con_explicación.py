print("\n   Bienvenidos al conversor de números Binario/Decimal.\n")

# Uso de menú interactivo
opcion=""
while opcion!="3":
        print("1. Convertir de Decimal a Binario")
        print("2. Convertir de Binario a Decimal")
        print("3. Salir del Conversor")
        opcion = input("\nSeleccione la opción deseada (1, 2, 3): ").strip()
        
        # Validar una entrada válida en las opciones del menú    
        if not opcion.isdigit() or opcion not in ["1", "2", "3"]:
            print("Debe ingresar una opción válida.")
            continue  # vuelve al inicio del menú    
            
        # Opciones del menú
        match opcion:

            # De decimal a binario
            case "1":
                seguir = "s"
                # El usuario ingresa el número
                while seguir == "s":
                    num_decimal = input("Ingrese un número entero positivo, en base decimal: ").strip()

                    # Validación: el número ingresado sea un entero positivo y que la entrada no esté vacía
                    while not num_decimal.isdigit() or num_decimal=="":
                        print("Disculpa, pero no se ha ingresado una entrada válida")
                        num_decimal=input("Debe ingresar un número entero positivo en base decimal: ").strip()
                    
                    # Dar al usuario la posibilidad de ver la explicación
                    explicacion=input("¿Deseas ver la explicación? (s/n): ").strip().lower()
                    if explicacion == "s":
                        print("\nExplicación paso a paso:")
                    # Convertir el número decimal a binario
                    numero = int(num_decimal)

                    # Si el número es cero
                    if numero==0:
                       binario="0"
                    # Convertir el número decimal a binario
                    elif numero > 0:
                        binario = ""    # Trabajar con string para poder concatenar texto
                        while numero > 0:
                            resto = numero % 2       # Resto de la división 
                            if explicacion == "s":
                                print(f"{numero} dividido a 2 ", end="")
                            binario = str(resto) + binario   # Ir concatenando los restos de la división de derecha a izquierda
                            numero = numero // 2     # División truncada para mantener el entero y luego hacer la siguiente búsqueda del resto
                            if explicacion == "s":
                                print(f"es {numero}, el resto es {resto}")

                    # Dar el resultado al usuario
                    if explicacion == "s":
                        print("\nUnimos todos los restos: comenzando por el último hacia el primero y los escribimos de izquierda a derecha.")
                    print(f"\nEl número decimal {num_decimal} equivale en binario a {binario}")

                    seguir = input("\n¿Desea convertir otro número (para números mayores a cero)? (s/n): ").strip().lower()           

            # De binario a decimal
            case "2":
                seguir = "s"
                while seguir == "s":

                    #El usuario ingresa un número 
                    num_binario = input("\nIngrese un número binario: ").strip()
                   
                    # Valida que la entrada contenga un número binario y que la entrada no esté vacía                
                    while set(num_binario) - {"0", "1"} or num_binario=="":
                        print("\nDisculpa, pero no se ha ingresado una entrada válida")
                        num_binario=input("Debe ingresar un número binario: ").strip()
                    
                    # Dar al usuario la posibilidad de ver la explicación
                    explicacion=input("¿Deseas ver la explicación (para numeros mayores a cero)? (s/n): ").strip().lower()
                    print()

                    # convertir la cadena de texto a número e iniciar el pasaje de binario a decimal
                    numero = int(num_binario)
                    
                    # Cuando el número es cero
                    if numero == 0:
                        decimal=0
                    
                    #Cuando el número es mayor que cero
                    elif numero > 0:
                        decimal = 0
                        potencia = 0
                        if explicacion == "s":
                            print("\nExplicación paso a paso:")
                        for digito in reversed(num_binario):
                            paso = int(digito) * (2 ** potencia)
                            decimal += paso
                            if explicacion == "s":
                                print(f"{digito} x 2^{potencia} = {paso}")
                            potencia += 1

                    if explicacion == "s":
                        print("     Sumanos...")

                    # Dar el resultado al usuario
                    print(f"\nEl número binario {num_binario} equivale a {decimal} en decimal")
                    seguir = input("\n¿Desea convertir otro número? (s/n): ").strip().lower()

            # Para salir del programa
            case "3":
                print("¡Hasta Luego!")

            # Validación de entrada al menú 
            case _:
                print("\nDisculpa, pero la opción ingresada no es válida \nInténtalo nuevamente\n")