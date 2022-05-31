def between(a,b):
    my_count = a
    result = []
    for i in range(a, b+1):
        result.append(my_count)
        my_count += 1
    return result


print(between(1, 4))
print(between(-4, 4))