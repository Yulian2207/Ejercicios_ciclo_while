#Ejercicio #03
num = int (input("Introduce un número entero positivo: "))
if num > 0:
    suma = 0
    i = 1
    while i <= num:
        if i % 3 == 0:
            suma += i
        i += 1
    print ("La suma de los números divisibles por 3 desde 1 hasta", num, "es: ", suma)
else:
    print ("Por favor, ingrese un número entero positivo")
