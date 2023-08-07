def all_equal(lst):
    if not lst:
        return True
    return all(x == lst[0] for x in lst)

# False, this is because our list is has not the same data
print(all_equal([1, 2, 1, 3, 4, 1, 4, 4, 1]))

# True because our list is the same data
print(all_equal([1, 1, 1, 1]))