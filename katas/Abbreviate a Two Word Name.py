def abbrev_name(name):
    nick = name
    surname = name.split()
    return nick[0][0].upper() + "." + surname[1][0].upper()


print(abbrev_name("Sam Harris"))
print(abbrev_name("patrick feenan"))
print(abbrev_name("Evan C"))
print(abbrev_name("P Favuzzi"))
print(abbrev_name("David Mendieta"))