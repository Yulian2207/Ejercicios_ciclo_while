#Ejercicio #15

num = int (input("Introduce un número entero positivo: "))
if num > 0:
    suma = 0
    contador = 0
    i = 1
    while i <= num:
        suma += i
        contador += 1
        i += 1
    promedio = suma / contador 
    print (f"El promedio de los numeros desde 1 hasta {num} es: {promedio}")
else:
    print ("Por favor, ingrese un numero entero positivo.")
