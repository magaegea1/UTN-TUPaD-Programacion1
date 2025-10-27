#Tp 9 - Recursividad - TUPaD
print("\n--- TP 9 - Recursividad ---\n")

#-------------------------------------------------------------------------
# Actividad 1.Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
# función para calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario 

print("_"*40, "\n")
print(f"Actividad 1\n")
print("¡Hola!\n")

# Función recursiva para calcular el factorial de un número.
def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
    
# Función para validar que el usuario ingrese un número entero positivo menor que 999, se verificó que hasta
# ahí se puede usar la función recursiva    
def validar_entero_positivo_1a998():
    valido=False
    while not valido:
        num=input().strip()
        try:
            numero=int(num)
            if 0<numero<999:   # 0 no es un número entero positivo
                return numero
            else:
                print(f"Disculpe, pero {numero} no es un número entero entre 1 y 998, intente nuevamente: ", end="")
        except ValueError:
            print("Disculpe, pero no ha ingresado un número entero entre 1 y 998, intente nuevamente: ", end="")

# Calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario
print("Ingrese un número entero entre 1 y 998 para calcular el factorial desde 1 hasta ese número: ", end="")
numero=validar_entero_positivo_1a998()
for i in range(1,numero+1):
    print(f"El factorial de {i} es: {factorial(i)}")

print("\n¡Muchas gracias y hasta luego!\n")

#----------------------------------------
# Actividad 2. Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
# especifique. 

print("_"*40, "\n")
print(f"Actividad 2\n")
print("¡Hola!\n")

# Función para calcular el valor de la serie de Fibonacci en la posición indicada
def fibonacci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
    
# Pedir al usuario un número entre 0 y 35, porque más de 35 tarda mucho en aparecer el resultado
print(f"Ingresa un número entero entre 1 y 35 para ver la serie de Fibonacci hasta esa posición: ", end="")   
def validar_entre_1y35():
    valido=False
    while not valido:
        num=input().strip()
        try:
            numero=int(num)
            if 0<numero<36:   
                return numero
            else:
                print(f"Disculpe, pero {numero} no es un número entero entre 1 y 35, intente nuevamente: ", end="")
        except ValueError:
            print("Disculpe, pero no ha ingresado un número entero entre 1 y 35, intente nuevamente: ", end="")

numero=validar_entre_1y35()

#  Mostrar la serie completa hasta la posición dada
print(f"\nLa serie de Fibonacci hasta la posición {numero} es: ", end="")
for i in range(numero):   
    print(f"{fibonacci(i)} ", end="") 

print("\n¡Muchas gracias y hasta luego!\n")

#----------------------------------------
# Actividad 3. Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛**𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
# algoritmo general. 

print("_"*40, "\n")
print(f"Actividad 4\n")
print("¡Hola!\n")

# Definir la función potencia, donde bas=base y exp=exponente de la potencia
# Esta función sólo trabaja con exponentes enteros
def potencia(bas,exp):
    if exp<0 and bas!=0:
        return 1/potencia(bas,-exp)
    elif bas==0:
        if exp==0:
            return "Indeterminado"
        elif exp<0:
            return "No se puede dividir entre 0"
        else:
            return 0
    elif bas==1 or exp==0:
        return 1
    else:
       return bas*potencia(bas,exp-1)

            

print("\nProbando la función de potencia usando recursividad:")    
print(f"2 elevado a la 6: {potencia(2,6)}")
print(f"0 elevado a la 0: {potencia(0,0)}")
print(f"0 elevado a la 5: {potencia(0,5)}")
print(f"1 elevado a la 0: {potencia(1,0)}")
print(f"1 elevado a la 45: {potencia(1,45)}")
print(f"-1 elevado a la 45: {potencia(-1,45)}")
print(f"-3 elevado a la 4: {potencia(-3,4)}")
print(f"-3 elevado a la 3: {potencia(-3,3)}")
print(f"2 elevado a la -1: {potencia(2,-1)}")
print(f"2 elevado a la -3: {potencia(2,-3)}")
print(f"1 elevado a la -1: {potencia(1,-3)}")
print(f"0 elevado a la -4: {potencia(0,-4)}")

print("\n¡Muchas gracias y hasta luego!\n")

#----------------------------------------
# Actividad 4. Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto. 

print("_"*40, "\n")
print(f"Actividad 4\n")
print("¡Hola!\n")

# Fución recursiva para convertir un número entero positivo decimal en binario
def convertir_a_binario(decimal):
    if decimal<0:
        return "Disculpe, pero sólo funciona con numeros enteros positivos en base 10"   
    elif decimal==0:
        return "0"
    elif decimal==1:
        return "1"
    else:
       return f"{convertir_a_binario(decimal//2)}{decimal%2}"
    
print(f"El número decimal 13 en binario es: {convertir_a_binario(13)}")
print(f"El número decimal 0 en binario es: {convertir_a_binario(0)}")
print(f"El número decimal 1 en binario es: {convertir_a_binario(1)}")
print(f"El número decimal -13 en binario es: {convertir_a_binario(-13)}")

print("\n¡Muchas gracias y hasta luego!\n")

#----------------------------------------
# Actividad 5.Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
# lo es. 
# Requisitos: 
# La solución debe ser recursiva. 
# No se debe usar [::-1] ni la función reversed(). 

print("_"*40, "\n")
print(f"Actividad 5\n")
print("¡Hola!\n")

# Para poder limpiar la cadena de texto, sin tildes, se importará unicodedata
import unicodedata

# Función para limpar texto, se eliminarán espacios y tildes 
def limpiar_texto(texto):
    texto=texto.strip().lower()
    texto="".join(texto.split()) #Elimina espacios internos o saltos
    texto=unicodedata.normalize("NFD",texto) #Para separar letras de los acentos o similares
    texto="".join(letra for letra in texto if unicodedata.category(letra) != 'Mn') #para unir quitando acentos
    return texto

# Función que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo 
# o False si no lo es
def es_palindromo(palabra):
    palabra_limpia=limpiar_texto(palabra)
    longitud=len(palabra_limpia)
    #Por si quedó una cadena vacía luego de limpiar y en caso de que haya un sólo caracter
    if longitud<=1: 
        #Por definición de Palídromo, si está vacía o tiene un sólo caracter es palíndromo
        return True
    if palabra_limpia[0]!=palabra_limpia[-1]:
        return False
    #De forma recursiva recorta los extremos de la cadena de texto
    return es_palindromo(palabra_limpia[1:-1]) 

print("¿Es Palíndromo?\n")
print(f"1.-     : {es_palindromo("    ")}")
print(f"2.- a: {es_palindromo("a")}")
print(f"3.-    b    : {es_palindromo("   b    ")}")
print(f"4.- Reconocer: {es_palindromo("Reconocer")}")
print(f"5.-   AÉREOpuerto   : {es_palindromo("   AÉREOpuerto   ")}")
print(f"6.-   AÉREA   : {es_palindromo("   AÉREA   ")}")
print(f"7.- Ne    U q U é N: {es_palindromo(" Ne    U q U é N")}")
print(f"8.- Anita lava la tina: {es_palindromo(" Anita lava la tina")}")
print(f"9.- Yo HAGO y o g a HOY: {es_palindromo("Yo HAGO y o g a HOY")}")
print(f"10.- Yo HAGO y o g a HOY a la tarde: {es_palindromo("Yo HAGO y o g a HOY a la tarde")}")

print("\n¡Muchas gracias y hasta luego!\n")


#----------------------------------------
# Actividad 6. Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
# número entero positivo y devuelva la suma de todos sus dígitos. 
#      Restricciones: 
# No se puede convertir el número a string. 
# Usá operaciones matemáticas (%, //) y recursión. 
# Ejemplos: 
# suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
# suma_digitos(9)      → 9 
# suma_digitos(305)    → 8   (3 + 0 + 5) 

print("_"*40, "\n")
print(f"Actividad 6\n")
print("¡Hola!\n")

def suma_digitos(n):
    if n<10:
        return n
    else:
        return suma_digitos(n//10) + n%10

print(f"1234 = 1 + 2 + 3 + 4 = {suma_digitos(1234)}")
print(f"9 = {suma_digitos(9)}")
print(f"305 = 3 + 0 + 5 = {suma_digitos(305)}")   

print("\n¡Muchas gracias y hasta luego!\n")

#----------------------------------------
# Actividad 7. Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
# último nivel con un solo bloque. 
 
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
# pirámide. 
 
#       Ejemplos: 
# contar_bloques(1)   → 1         (1) 
# contar_bloques(2)   → 3         (2 + 1) 
# contar_bloques(4)   → 10        (4 + 3 + 2 + 1)

print("_"*40, "\n")
print(f"Actividad 7\n")
print("¡Hola!\n")

def contar_bloques(n):
    if n==0:
        return 0
    elif n<0:
        return "Disculpe, hay un error, no puede haber una cantidad de bloques negativa"
    else:
        return n + contar_bloques(n-1)
        

print("Ejemplos de contar bloques:\n")
print(f"1. si hay 1 bloque: {contar_bloques(1)}") 
print(f"2. si hay 4 bloques: 4 + 3 + 2 + 1 = {contar_bloques(4)}")
print(f"3. si hay 7 bloques: 7 + 6 + 5 + 4 + 3 + 2 + 1 = {contar_bloques(7)}") 
print(f"4. si hay 0 bloques: {contar_bloques(0)}")
print(f"5. si hay -3 bloque: {contar_bloques(-3)}")

print("\n¡Muchas gracias y hasta luego!\n")

#----------------------------------------
# Actividad 8.  Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
# aparece ese dígito dentro del número. 
#      Ejemplos: 
# contar_digito(12233421, 2)   → 3   
# contar_digito(5555, 5)       → 4   
# contar_digito(123456, 7)     → 0   

print("_"*40, "\n")
print(f"Actividad 8\n")
print("¡Hola!\n")

def contar_digito(numero, digito):
    numero=abs(numero)
    if digito<0 or digito>10:
        return "Disculpe, hay un error: El dígito debe estar entre 0 y 9"
    if numero<10:
        return 1 if numero==digito else 0
    else:
        return (1 if numero%10==digito else 0) + contar_digito(numero//10, digito)

print("Ejemplos de contar dígitos en un número:\n")
print(f"1. En el número 12233421, el dígito 2 aparece: {contar_digito(12233421, 2)} veces") 
print(f"2. En el número 5555, el dígito 5 aparece:  {contar_digito(5555, 5)} veces")
print(f"2. En el número 123456, el dígito 7 aparece:  {contar_digito(123456, 7)} veces") 
print(f"3. En el número 0, el dígito 0 aparece:  {contar_digito(0, 0)} veces")
print(f"4. En el número -132334353, el dígito 3 aparece:  {contar_digito(-132334353, 3)} veces")
print(f"3. En el número 12345, el dígito -3 aparece:  {contar_digito(12345, -3)} veces")
print(f"3. En el número 12345, el dígito 12 aparece:  {contar_digito(12345, 12)} veces")

print("\n¡Muchas gracias y hasta luego!\n")



