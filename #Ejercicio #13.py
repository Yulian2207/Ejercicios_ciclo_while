#Ejercicio #13

num1 = int (input("Introduce el primer número entero positivo: "))
num2 = int (input("Introduce el segundo número entero positivo: "))
if num1 > 0 and num2 > 0:
    print (f"Tabla de multiplicar de {num1} hasta {num2}:")
    i = 1
    while i <= num2:
        resultado = num1 * i
        print (f"{num1} x {i} = {resultado}")
        i += 1
else:
    print ("Ingrese un número entero positivo.")


