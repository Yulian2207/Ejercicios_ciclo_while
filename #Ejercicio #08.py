#Ejercicio #08
num = int (input("Introduce un número entero positivo: "))
if num > 0:
    i = 1
    contador = 0
    while contador < num:
        print (i)
        i += 2
        contador += 1
else: 
    print ("Por favor, ingrese un numero entero positivo")