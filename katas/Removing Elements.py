def remove_every_other(my_list):
    result = []
    for element in range(len(my_list)):
        if element % 2 == 0:
            result.append(my_list[element])

    return result





print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))