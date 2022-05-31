def digital_root(n):
    if n <= 0:
        return 0
    else:
        return n  % 9


print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))