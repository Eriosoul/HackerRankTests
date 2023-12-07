import random
import string
def search_number(list_, n):
    found = False
    for i in list_:
        if i == n:
            found = True
            print(f"Se ha encontrado {n} en la lista")
            break
    return found

random_num = random.randint(1,40)
print(f"El numero random es: {random_num}")
num = list(range(0, 40))
print(search_number(num, random_num))


length = 2
def search_letter(random_letter, char_to_find):
    found_letter = False
    for char in string.ascii_letters:
        if char == char_to_find:
            found_letter = True
            break
    return found_letter

characters = string.ascii_letters
random_letter = ''.join(random.choices(string.ascii_letters, k=length))
print(f"La letra aleatoria es: {random_letter}")

for char in string.ascii_letters:
    found_char = search_letter(random_letter, char)
    if found_char:
        break
    break
