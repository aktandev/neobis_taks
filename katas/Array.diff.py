def array_diff(a, b):
    true = []
    if len(a) == 0:
        return []
    elif len(b) == 0:
        return a

    for num in a:
        if num not in b:
            true.append(num)

    return true

print(array_diff([1,2], [1]))
print(array_diff([1,2,2], [2]))