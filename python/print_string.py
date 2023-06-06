"""
The included code stub will read an integer, n, from STDIN.

Without using any string methods, try to print the following:
123 · · · n

Note that "..." represents the consecutive values in between.

Example
n = 5
Print the string 12345.


"""
n = 5
lista: list = []
for i in range(n):
    lista.append(i + 1)

string_lista = ''.join(str(elemento) for elemento in lista)
print(string_lista)
