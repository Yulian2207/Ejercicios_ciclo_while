#Ejercicio #04

num = int (input("Introduce un número entero positivo: "))
if num > 0:
    num_str = str (num)
    num_digitos = len (num_str)
    suma = 0
    n = num 
    while n > 0:
        digito = n % 10
        suma += digito ** num_digitos
        n //= 10
    if suma == num:
        print (f"{num} es un número de Armstrong.")
    else:
        print (f"{num} no es un número de Armstrong.")
else:
    print ("Por favor, ingrese un número entero positivo.")