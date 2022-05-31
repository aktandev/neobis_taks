def has_unique_chars(string):
    unique_chars = set()
    for elem in string:
        if elem in unique_chars:
            return False
        unique_chars.add(elem)
    return True