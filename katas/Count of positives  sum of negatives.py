def count_positives_sum_negatives(arr):
    positive=0
    negative=0
    for i in arr:
        if i < 0:
            negative += i
        elif i > 0:
            positive += 1
    if len(arr) == 0:
        result = []
    else:
        result =[positive, negative]
    return result


print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))
print(count_positives_sum_negatives([1]))
print(count_positives_sum_negatives([-1]))
print(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]))
print(count_positives_sum_negatives([]),)