"""
Ejercicio: Suma de Números Pares e Impares

Escribe un programa que solicite al usuario ingresar un número entero positivo.
Luego, calcula la suma de todos los números pares e impares desde 1 hasta el número ingresado, y finalmente imprime ambas sumas.
"""


array_par = []
array_impar = []

while True:
    option = input("Introduce más números: Y(yes) N(no): ").upper()

    if option == "N":
        break  # Sale del bucle si la opción es "N"
    elif option == "Y":
        num = int(input("Número: "))
        if num % 2 == 0:
            print(f"{num} es par")
            array_par.append(num)
        else:
            print(f"{num} es impar")
            array_impar.append(num)
    else:
        print("Opción no válida. Ingresa 'Y' para sí o 'N' para no.")

print("Array de números pares:", array_par)
sum_par = sum(array_par)
print(f"La suma de {array_par} da un resultado de {sum_par}")
print("Array de números impares:", array_impar)
sum_impar = sum(array_impar)
print(f"La suma de {array_impar} da un resultado de {sum_impar}")
