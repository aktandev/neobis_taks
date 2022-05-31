def find_it(seq):
    result = 0
    for elem in seq:
        result ^= elem
    return result




print(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))