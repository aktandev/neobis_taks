from functools import reduce
from math import gcd
def sum_two(f1, f2):
    n1, d1 = f1
    n2, d2 = f2
    n = n1 * d2 + n2 * d1
    d = d1 * d2
    return [n // gcd(n, d), d // gcd(n, d)]
def sum_fracts(lst):
    if not lst:
        return None
    result = reduce(sum_two, lst)
    if result[1] == 1:
        return result[0]
    return result