def infected(s):
    oceans = s.split('X')
    infected = 0
    safe = 0
    for ocean in oceans:
        if '1' in ocean:
            infected += len(ocean)
        else:
            safe += len(ocean)
    if infected + safe == 0:
        return 0
    return infected/(infected+safe)*100

print(infected("01000000X000X011X0X"))

