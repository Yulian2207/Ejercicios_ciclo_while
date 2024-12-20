#Ejercicio #01

num = int(input("Ingrese un número entero: "))
if num > 0:
    i = 1
    while i <= num:
        if i % 5 == 0:
            print(i)
        i += 1
else: 
        print ("Por favor ingrese un número entero positivo")
