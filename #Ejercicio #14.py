#Ejercicio #14
num = int (input("Introduce un número entero positivo: "))
if num > 0:
    a, b = 0, 1
    suma = 0
    while a <= num:
         suma += a
         a, b = b, a + b
    print (f"La suma de los números de Fibonacci hasta {num} es: {suma}")
else:
     print ("Por favor, ingrese un número entero positivo.")
