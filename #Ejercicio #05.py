#Ejercicio #05

num = int (input("Introduce un número entero positivo: "))
if num > 0:
    def es_primo (n):
        if n <= 1:
            return False
        divisor = 2
        while divisor * divisor <= n:
            if n % divisor == 0:
                return False
            divisor += 1
        return True
    i = 2
    while i <= num:
        if es_primo (i):
            print (i)
        i += 1
else:
    print ("Por favor, ingrese un número entero positivo")