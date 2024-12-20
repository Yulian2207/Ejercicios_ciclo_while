#Ejercicio #10

num1 = int (input("Introduce un número entero positivo: "))
num2 = int (input("Introduce un número entero positivo: "))
if num1 > 0 and num2 > 0:
    if num1 > num2:
        num1, num2 = num2, num1
    suma = 0
    i = num1 + 1
    while i < num2:
        suma += i
        i += 1
    print (f"La suma de los números entre {num1} y {num2} es: {suma}")
else:
    print ("Por favor, ingrese un número entero positivo.")
