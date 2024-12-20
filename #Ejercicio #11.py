#Ejercicio #11

num = int (input("Introduce un número entero positivo: "))
if num > 0:
    cantidad_digitos = 0
    while num > 0:
        cantidad_digitos += 1
        num //= 10
    print (f"La cantidad de dígitos del número es: {cantidad_digitos}")
else:
    print ("Por favor, ingrese un número entero positivo.")