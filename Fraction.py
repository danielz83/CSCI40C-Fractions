class Fraction(object):
    # if denominator is none, then you want to assume that the denominator is 1
    def __init__(self, numerator=0, denominator=1):
        #TODO: denominator is none, then you want to assume that denominator is 1
        if isinstance(numerator,int) and isinstance(denominator,int):
            if denominator == 0:
                raise ZeroDivisionError("Denominator can't be zero")
        elif isinstance(numerator,str):
            fraction_str = numerator.strip()
            if '/' in fraction_str:
                try:
                    numerator_str, denominator_str = fraction.split('/')
                except ValueError:
                    self.numerator = 0
                    self.denominator = 1
            return
                
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
