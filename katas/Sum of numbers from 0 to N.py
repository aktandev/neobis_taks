def show_sequence(n):
    if n < 0:
        return str(n) + "<0"
    if n == 0:
        return str(n) + "=0"

    result = sum(range(n + 1))
    n_str = "+".join(map(str, range(n + 1)))

    return n_str + " = " + str(result)


print(show_sequence(32))