def two_decimal_places(number):
    my_str = str(number).split('.')
    result = my_str[0] + '.' + my_str[1][0] + my_str[1][1]
    return float(result)






print(two_decimal_places(10.1289767789))
print(two_decimal_places(-7488.83485834983))
print(two_decimal_places(4.653725356))