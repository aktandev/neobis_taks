def summation(num):
    my_count0 = -1
    my_count = 0
    for sum in range(num):
        my_count0 += 1
        my_count +=1
        my_count += my_count0
    return my_count



print(summation(100))