def find(n):
    result = 0
    for element in range(n+1):
        if element % 3 == 0 or element % 5 == 0:
            result += element
    return result




print(find(5))
print(find(10))