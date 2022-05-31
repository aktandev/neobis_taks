def sum_of_minimums(numbers):
    sum = 0
    for num in numbers:
        sum += min(num)
    return sum

print(sum_of_minimums([[7, 9, 8, 6, 2],[6, 3, 5, 4, 3],[5, 8, 7, 4, 5]]))