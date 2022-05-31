def xo(s):
    x_counter, o_counter = 0, 0

    for letter in range(len(s)):
        if 'x' in s[letter].lower():
            x_counter += 1
        elif 'o' in s[letter].lower():
            o_counter += 1

    if x_counter == o_counter:
        return True
    else:
        return False


print(xo('xxoo'))
print(xo('xxoo'))
print(xo('xxooo'))
print(xo('xXOo'))
print(xo('dimon'))