def check_exam(arr1,arr2):
    score = 0

    for i in range(len(arr1)):
        if arr2[i] == "":
            score += 0
        elif arr1[i] == arr2[i]:
            score += 4
        elif arr1[i] != arr2[i]:
            score -= 1

    if score < 0:
        return 0
    else:
        return score

print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", ""]))