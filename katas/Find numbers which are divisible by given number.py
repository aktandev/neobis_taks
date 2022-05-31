def divisible_by(numbers, divisor):
    divisible_list = []
    for element in numbers:
        if element % divisor == 0:
            divisible_list.append(element)
    return divisible_list

print(divisible_by([1,2,3,4,5,6], 2))
print(divisible_by([1,2,3,4,5,6], 3))
print(divisible_by([0,1,2,3,4,5,6], 4))
print(divisible_by([0], 4))
print(divisible_by([1,3,5], 2))
print(divisible_by([0,1,2,3,4,5,6,7,8,9,10], 1))