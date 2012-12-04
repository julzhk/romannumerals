r2i = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

thousands_looktable= {
    0: ('', '', ''),
    1: ('I', 'X', 'C'),
    2: ('II', 'XX', 'CC'),
    3: ('III','XXX','CCC' ),
    4: ('IV', 'XL', 'CD'),
    5: ('V', 'L', 'D'),
    6: ('VI', 'LX', 'DC'),
    7: ('VII', 'LXX', 'DCC'),
    8: ('VIII', 'LXXX', 'DCCC'),
    9: ('IX', 'XC', 'CM'),
}

class RomanNumeral(object):

    def __init__(self, n):
        if isinstance(n, int):
            self.r = self.int2roman(n)
            self.i = n
        elif isinstance(n, str):
            self.r = n
            self.i = self.roman2int(n)
        elif isinstance(n, RomanNumeral):
            self.r = n.r
            self.i = n.i

    def __eq__(self, other):
        o = RomanNumeral(other)
        return self.i == o.i and self.r == o.r

    def __lt__(self, other):
        return self.i < RomanNumeral(other).i

    def __gt__(self, other):
        return self.i > RomanNumeral(other).i

    def __iadd__(self, other):
        self.i += RomanNumeral(other).i
        self.r = int2roman(self.i)
        return self

    def int2roman(self, x):
        return ''.join(reversed([
            thousands_looktable[
                int(digit)][power]
                    for power, digit in enumerate(reversed(str(x)
            ))]))

    def roman2int(self, r):
        n = 0
        current = r2i[r[0]]
        for c in r[1:]:
            prev = current
            current = r2i[c]
            if current > prev:
                n -= prev
            else:
                n += prev
        n += current
        return n
