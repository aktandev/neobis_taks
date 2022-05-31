def paul(x):
    paul_rules = {'life': 0, 'eating': 1, 'kata': 5, 'Petes kata': 10}
    score = (sum(map(paul_rules.get, x)))
    if score < 40:
        return 'Super happy!'
    elif score < 70:
        return "Happy!"
    elif score < 100:
        return "Sad!"
    return "Miserable!"



# 'kata' = 5
# 'Petes kata' = 10
# 'life' = 0
# 'eating' = 1

# 40 = 'Super happy!'
# < 70 >= 40 = 'Happy!'
# < 100 >= 70 = 'Sad!'
# > 100 = 'Miserable!'


print(paul(['life', 'eating', 'life','Petes kata', 'Petes kata','Petes kata','Petes kata','Petes kata','Petes kata',
            'Petes kata','Petes kata','Petes kata','Petes kata','Petes kata']))