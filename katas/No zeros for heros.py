def no_boring_zeros(n):
    # n_str = str(n)
    # is_zero = n_str == "0"
    # return 0 if is_zero else int(n_str.strip("0"))
    try:
        return int(str(n).rstrip('0'))
    except ValueError:
        return 0

    
print(no_boring_zeros(1450))
print(no_boring_zeros(960000))