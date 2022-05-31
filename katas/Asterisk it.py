def asterisc_it(n):
    if type(n) == list:
        n = "".join([str(e) for e in n])
    s = ""
    n = str(n)
    for i in range(len(n)-1):
        if int(n[i]) % 2 == 0 and int(n[i+1]) % 2 == 0:
            s = s + n[i] + "*"
        else:
            s = s + n[i]
    return s + n[-1]   




print(asterisc_it(2222))