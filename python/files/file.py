with open('ninja.txt', 'w+') as cn:
    print(cn.read())
# create a list to get the info
append_info = []
fileopened= open("FILENAME.txt",'w', encoding="utf-8")

try:
    while True:
        escitura = input('Para salir escriba exit'
                         'Escriba ahora: ')
        if escitura == "exit":
            break
        append_info.append(escitura + '\n')

    for line in append_info:
        fileopened.write(line)
finally:
    fileopened.close()

# fileopened = open('FILENAME.txt', 'r')
# print(fileopened.read())
