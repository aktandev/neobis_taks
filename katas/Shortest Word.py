def find_short(s):
    my_list = list(s.split())
    return len(min(my_list, key=len))

    # shortest_word = min(my_list, key=len)
    # letter_counter = 0
    # for i in range(len(shortest_word)):
    #     letter_counter += 1
    # return letter_counter




print(find_short("bitcoin take over the world maybe who knows perhaps"))
print(find_short("turns out random test cases are easier than writing out basic ones"))
print(find_short("lets talk about javascript the best language"))
print(find_short("i want to travel the world writing code one day"))
print(find_short("Lets all go on holiday somewhere very cold"))
print(find_short("Let's travel abroad shall we"))