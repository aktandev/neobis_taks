def sum_even_numbers(seq):
    return sum(integer for integer in seq if not integer % 2)


print(sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sum_even_numbers([]))