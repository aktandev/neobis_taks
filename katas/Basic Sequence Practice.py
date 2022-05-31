def sum_of_n(n):
    my_list = [0]
    my_sum = 0
    if n >= 0:
        for elem1 in range(1, n + 1):
            my_sum += elem1
            my_list.append(my_sum)
    else:
        n = -n
        for elem2 in range(1, n + 1):
            my_sum += elem2
            my_list.append(-my_sum)
    return my_list




print(sum_of_n(3))
print(sum_of_n(-4))
print(sum_of_n(1))
print(sum_of_n(0))
print(sum_of_n(10))