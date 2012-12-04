r2i = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

class RomanNumeral(object):

    def __init__(self, r):
        self.r = r
        self.i = r2i[r]

    def __eq__(self, other):
        return self.i == other.i

    def __lt__(self, other):
        return self.i < other.i

    def __gt__(self, other):
        return self.i > other.i

def roman2int(r):
    n = 0
    current = RomanNumeral(r[0])
    for c in r[1:]:
        prev = current
        current = RomanNumeral(c)
        if current > prev:
            n -= prev.i
        else:
            n += prev.i
    n += current.i
    return n
