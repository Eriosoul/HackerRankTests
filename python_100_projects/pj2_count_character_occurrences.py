def count_characters(c):
    # count variable tipo dicionario que almacenara los resultados
    count:dict = { }
    # bule for para inicializar el conteo
    for i in c:
        # si letra esta mas de una vez en palabra suma 1
        if i in count:
            count[i] +=1
        # si letra no esta mas de una vez en palabra pon 1
        else:
            count[i] = 1
    print(count)
print(count_characters("Thecleverprogrammer"))
