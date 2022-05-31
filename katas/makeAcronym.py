def make_acronym(phrase):
    my_list = []
    if type(phrase) != str:
        return 'Not a string'
    if phrase == "":
        return ""
    if not phrase.replace(' ', '').isalpha():
        return "Not letters"

    for e in phrase.split():
        my_list.append(e[0][0])
    return ''.join(my_list).upper()




print(make_acronym('My aunt sally'))
print(make_acronym('Please excuse my dear aunt Sally'))
print(make_acronym('How much wood would a woodchuck chuck if a woodchuck could chuck wood'))