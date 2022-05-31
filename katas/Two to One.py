def longest(a1, a2):
    uniques = set(a1 + a2)
    return ''.join(sorted(uniques))



print(longest("aretheyhere", "yestheyarehere"))