def accum(s):
    s_str = ''
    for i in range(0, len(s)):
        s_str += s[i].upper()
        s_str += s[i].lower()*i
        if i != len(s)-1:
            s_str += "-"
    return s_str



print(accum("ZpglnRxqenU"))