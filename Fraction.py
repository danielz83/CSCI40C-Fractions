class Fraction(object):
    # if denominator is none, then you want to assume that the denominator is 1
    def __init__(self, numerator=0, denominator=1):
        #TODO: denominator is none, then you want to assume that denominator is 1

        if denominator is None:
            if isinstance(numerator, int):
                self.numerator = numerator
                self.denominator = denominator

    def gcd(a, b):
        #TODO
        pass

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass