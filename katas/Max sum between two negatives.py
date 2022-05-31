def max_sum_between_two_negatives(arr):
    current_sum = 0
    seen_negative = False
    results = [-1]
    for element in arr:
        if element > 0 and seen_negative:
            current_sum += element
        if element < 0 and seen_negative:
            results.append(current_sum)
            current_sum = 0
        if element < 0 and not seen_negative:
            seen_negative = True
    return max(results)

print(max_sum_between_two_negatives([-1,6,-2,3,5,-7]))