#Ejercicio #07
num = int (input("Introduce un número entero positivo: "))
if num > 0:
    suma = 0
    i = 2
    contador = 0
    while contador < num:
        suma += i
        i += 2
        contador = 1
    print (f"La suma de los primeros {num} números pares es: {suma}")
else: print ("Por favor, ingresa un número entero positivo")
