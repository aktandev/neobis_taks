from fractions import Fraction as Frg

class Fraction:

    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator

    # Equality test

    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num

    # The rest goes here

    # Happy Coding ;)

print(Fraction(1, 8) + Fraction(4, 5))