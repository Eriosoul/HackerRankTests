def triple_and(a, b, c):
    return a and b and c

result1 = triple_and(True, True, True)
result2 = triple_and(False, False, False)
result3 = triple_and(True, False, True)
print(result1, result2, result3)