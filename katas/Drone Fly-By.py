def fly_by(lamps, drone):
    drone_road = len(drone)
    switch = lamps.replace('x', 'o', drone_road)
    return switch

print(fly_by('xxxxxx', '====T'))
print(fly_by('xxxxxxxxx', '==T'))
print(fly_by('xxxxxxxxxxxxxxx', '=========T'))