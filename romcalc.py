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
        self.i = self.roman2int(r)

    def __eq__(self, other):
        if isinstance(other, int):
            return self.i == other
        return self.i == other.i

    def __lt__(self, other):
        if isinstance(other, int):
            return self.i < other
        return self.i < other.i

    def __gt__(self, other):
        if isinstance(other, int):
            return self.i > other
        return self.i > other.i

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
