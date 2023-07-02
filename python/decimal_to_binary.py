def binario(decimal_binary):
    binary = ""
    while decimal_binary // 2 != 0:
        binary = str(decimal_binary % 2) + binary
        decimal_binary = decimal_binary // 2
    return str(decimal_binary) + binary

def hexadecimal(decimal_hexa):
    hexa = ""
    while decimal_hexa // 16 != 0:
        hexa = str(decimal_hexa % 16) + hexa
        decimal_hexa = decimal_hexa // 16
    return str(decimal_hexa) + hexa


def octal(decimal_octal):
    octa = ""
    while decimal_octal // 8 != 0:
        octa = str(decimal_octal % 8) + octa
        decimal_octal = decimal_octal // 8
    return str(decimal_octal) + octa

num = int(input("Introduce un numero y se convertira a binario: "))

print(binario(num))
print(hexadecimal(num))
print(octal(num))

