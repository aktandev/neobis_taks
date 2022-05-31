def is_isogram(string):
    my_set = set(string.lower())

    if len(my_set) == len(string.lower()):
        return True
    else:
        return False


print(is_isogram("Dermatoglyphics"))
print(is_isogram("isogram"))
print(is_isogram("Dermatoglyphicsd"))