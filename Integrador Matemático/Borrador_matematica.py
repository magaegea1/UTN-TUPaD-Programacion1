print("Bienvenidos al conversor de números.")

opcion=""
while opcion!="3":
        print("1. Convertir de decimal a binario")
        print("2. Convertir de binario a decimal")
        print("3. Salir del conversor")
        opcion = input("Seleccione una opción (1, 2, 3): ").strip()
        if not opcion.isdigit():
            print("Debe ingresar una opción válida")    

        # Validar una entrada válida    
        if not opcion.isdigit() or opcion not in ["1", "2", "3"]:
            print("Debe ingresar una opción válida.")
            continue  # vuelve al inicio del menú    
            

        match opcion:

            case "1":
                seguir = "s"
                while seguir == "s":
                    num_decimal = input("ingrese un numero entero positivo en base decimal: ").strip()
                    while not num_decimal.isdigit():
                        print("El número ingresado no es válido")
                        num_decimal=input("Debe ingresar un numero entero positivo en base decimal: ").strip()

                    numero = int(num_decimal)
                    if numero==0:
                        binario="0"
                    elif numero > 0:
                        binario = ""
                        while numero > 0:
                            resto = numero % 2
                            binario = str(resto) + binario
                            numero = numero // 2

                    print(f"\nEl número en binario es: {binario}")
                    seguir = input("\n¿Desea convertir otro número? (s/n): ").strip().lower()           

            case "2":
                seguir = "s"
                while seguir == "s":
                    num_binario = input("ingrese un numero binario: ").strip()
                   
                    while num_binario=="":
                        print("El número ingresado no es válido")
                        num_binario=input("No puede estar vacío. Debe ingresar un numero binario: ").strip()
                   
                    while set(num_binario) - {"0", "1"}:
                        print("El número ingresado no es válido")
                        num_binario=input("Debe ingresar un numero binario: ").strip()
                    
                    numero = int(num_binario)
                    if numero == "0":
                        decimal=0
                    elif numero > 0:
                        decimal = 0
                        potencia = 0
                        for digito in reversed(num_binario):    #110
                            decimal += int(digito) * (2 ** potencia)    # 0*2^0  + 1 * 2^1  +  1
                            potencia += 1

                    print(f"El número binario {num_binario} equivale a {decimal} en decimal")
                    seguir = input("¿Desea convertir otro número? (s/n): ").strip().lower()

            case "3":
                print("¡Hasta Luego!")

            case _:
                print("\nDisculpa, pero la opción ingresada no es válida \nInténtalo nuevamente\n")