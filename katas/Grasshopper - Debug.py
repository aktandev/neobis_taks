def weather_info(temp):
    c = convert_to_celsius(temp)
    if c < 0:
        return str(c) + " is freezing temperature"
    else:
        return str(c) + " is above freezing temperature"

def convert_to_celsius(temperature):
    celsius = (temperature - 32) * (5/9.0)
    return round(celsius, 1)


print(weather_info(50))
print(weather_info(23))