def remove_consecutive_duplicates(s):
    s_list = []
    for elem in s.split(' '):
        if elem not in s_list:
            s_list.append(elem)
        elif s_list[-1] != elem:
            s_list.append(elem)
    return ' '.join(s_list)


print(remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))
