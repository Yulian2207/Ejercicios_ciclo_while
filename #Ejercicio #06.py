#Ejercicio #06

num = int (input("Introduce un número entero positivo: "))
if num > 0:
    suma = 0
    i = 1
    while i <= num:
        suma += i ** 2
        i += 1
    print (f"La suma de los cuadrados de los números desde 1 hasta {num} es: {suma}")
else: 
    print ("Por favor, ingrese un número entero positivo.")
