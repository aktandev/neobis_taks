def square_digits(num):
    pre_result = ''.join(str(int(i)**2) for i in str(num))
    return int(pre_result)
print(square_digits(9119))