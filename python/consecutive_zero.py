def consecutive_zeros(bin):
    return max(map(len, bin.split('1')))

bin = "10011000101001"
result = consecutive_zeros(bin)
print(result)