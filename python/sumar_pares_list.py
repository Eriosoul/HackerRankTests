"""
Ejercicio: Suma de Elementos Pares

Escribe una función llamada sumar_pares que tome una lista de números como argumento y devuelva la suma de todos los números pares en la lista. Luego, escribe un programa que solicite al usuario ingresar una lista de números, llame a la función sumar_pares y muestre el resultado.

Aquí hay un esquema básico para comenzar:

def sumar_pares(lista):
    # Tu código para sumar los números pares en la lista

# Solicitar al usuario ingresar una lista de números
entrada_usuario = input("Ingrese una lista de números separados por espacios: ")

# Convertir la entrada del usuario en una lista de números
numeros = [int(x) for x in entrada_usuario.split()]

# Llamar a la función y mostrar el resultado
resultado = sumar_pares(numeros)
print(f"La suma de los números pares es: {resultado}")
"""

def sumar_pares(lista):
    # check si los numero son pares
    numeros = [num for num in lista if num % 2 == 0]
    # Tu código para sumar los números pares en la lista
    return sum(numeros)

# Solicitar al usuario ingresar una lista de números
entrada_usuario = input("Ingrese una lista de números separados por espacios: ")

# Convertir la entrada del usuario en una lista de números
numeros = [int(x) for x in entrada_usuario.split()]

# Llamar a la función y mostrar el resultado
resultado = sumar_pares(numeros)
print(f"La suma de los números pares es: {resultado}")


#  usando una clase ahora

class CalculadoraNumeros:
    def sumar_pares(self, lista):
        numeros = [num for num in lista if num % 2 == 0]
        # Tu código para sumar los números pares en la lista
        return sum(numeros)

# Solicitar al usuario ingresar una lista de números
entrada_usuario = input("Ingrese una lista de números separados por espacios: ")

# Convertir la entrada del usuario en una lista de números
numeros = [int(x) for x in entrada_usuario.split()]

# Crear una instancia de la clase CalculadoraNumeros
calculadora = CalculadoraNumeros()

# Llamar al método sumar_pares y mostrar el resultado
resultado = calculadora.sumar_pares(numeros)
print(f"La suma de los números pares es: {resultado}")