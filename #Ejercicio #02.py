#Ejercicio #02

numero1 = int(input("Ingrese el primer número entero positivo: "))
numero2 = int(input("Ingrese el segundo número entero positivo: "))
if numero1 > 0 and numero2 > 0:
    if numero1 < numero2:
        i = numero1 + 1
        while i < numero2:
            print (i)
            i += 1
    elif numero1 > numero2:
        i = numero2 + 1
        while i > numero1:
            print (i)
            i += 1
    else:
        print ("Los dos números son iguales no hay rango entre ellos.")
else:
    print ("Por favor, ingrese dos números enteros positivos.")