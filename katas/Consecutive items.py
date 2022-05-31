def consecutive(arr, a, b):
    a_index = arr.index(a)
    b_index = arr.index(b)
    if a_index+1 == b_index or a_index-1 == b_index:
        return True
    else:
        return False



print(consecutive([1, 3, 5, 7], 3, 7))  # f
print(consecutive([1, 3, 5, 7], 3, 1))  # t
print(consecutive([1, 6, 9, -3, 4, -78, 0], -3, 4)) # t