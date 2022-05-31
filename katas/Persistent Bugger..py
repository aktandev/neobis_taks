def persistence(n):
    if n < 10:
        return 0
    n_str = str(n)
    total = 1
    for i in n_str:
        total = total * int(i)
    return 1 + persistence(total)


print(persistence(39))
print(persistence(4))
print(persistence(25))
print(persistence(999))