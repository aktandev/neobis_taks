def hydrate(drink_string):
    total_drank = []

    for elem in drink_string:
        if elem.isdigit():
            total_drank.append(elem)

    for element in range(0, len(total_drank)):
        total_drank[element] = int(total_drank[element])

    if sum(total_drank) > 1:
        return f"{sum(total_drank)} glasses of water"
    else:
        return f"{sum(total_drank)} glass of water"



print(hydrate("1 beer"))
print(hydrate("1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer"))