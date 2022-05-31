def cat_mouse(x):
    return 'Escaped!' if len(x) > 5 else 'Caught!'


    # if cat+1 == mouse or cat+2 == mouse or cat+3 == mouse or cat+3 == mouse or  cat+4 == mouse:
    #     return 'Caught!'
    # elif cat-1 == mouse or cat-2 == mouse or cat-3 == mouse or cat-4 == mouse:
    #     return 'Caught!'
    # else:
    #     return 'Escaped!'




print(cat_mouse('C....m'))
print(cat_mouse('C..m'))
print(cat_mouse('C.....m'))
print(cat_mouse('C.m'))
print(cat_mouse('m...C'))

