"""
Solicita al usuario ingresar un número entero.
Verifica si el número ingresado es mayor que 1 (los números primos deben ser mayores que 1).
Utiliza un bucle para verificar si el número es divisible por algún otro número menor que él.
Muestra un mensaje indicando si el número es primo o no.
"""

es_primo = True
num = int(input("Introduce un numero: "))
if num > 1:
    for i in range(2, int(num**0.5) +1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"{num} es un número primo.")
    else:
        print(f"{num} no es un número primo.")
else:
    print("Error: Debe introducir un número mayor que 1.")