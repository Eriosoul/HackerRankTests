import random

letras = " abcdefghijklmnñopqrstuvwxyz"
numeros = "0123456789"
simbolos = "·@#=<>{[]}?¿-;}][]}"

unir = f'{letras}{numeros}{simbolos}'
longitud = 10
contraseña = random.sample(unir, longitud)
password_final = "".join(contraseña)
print(password_final)