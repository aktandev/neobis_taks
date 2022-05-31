def count_sheeps(sheep):
    counting_my_sheeps = 0
    for sheep_is_here in sheep:
        if sheep_is_here == True:
            counting_my_sheeps += 1
    return counting_my_sheeps

