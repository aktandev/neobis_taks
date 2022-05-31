def cat_mouse(x,j):
    d, c, m = x.find('D'), x.find('C'), x.find('m')
    if -1 in [d, c, m]:
        return 'boring without all three'
    if abs(c - m) <= j:
        return 'Protected!' if c < d < m or m < d < c else 'Caught!'
    return 'Escaped!'

print(cat_mouse('..D.....C.m', 2))  # c
print(cat_mouse('............C.............D..m...', 8) ) # e
print(cat_mouse('m.C...', 5))  # b
print(cat_mouse('.CD......m.', 10))  # p
print(cat_mouse('.CD......m.', 1),)  # e