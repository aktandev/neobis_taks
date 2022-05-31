def digitize(n):
    digit_to_str = str(n)
    from_str_to_list = []
    for result in digit_to_str[::-1]:
        from_str_to_list.append(int(result))
    return from_str_to_list


print(digitize(345))
