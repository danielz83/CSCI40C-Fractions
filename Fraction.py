class Fraction(object):
    
    # if denominator is none, then you want to assume that the denominator is 1
    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator,int) and isinstance(denominator,int):
            if denominator == 0:
                raise ZeroDivisionError("Denominator can't be zero")
            else:
                self.numerator = numerator
                self.denominator = denominator

        elif isinstance(numerator, str):
            stringed_fraction = numerator.strip()
            if '/' in stringed_fraction:
                numerator_str, denominator_str = stringed_fraction.split('/',1)
                try:
                    self.numerator = int(numerator_str)
                    self.denominator = int(denominator_str)
                except ValueError:
                    self.numerator = 0
                    self.denominator = 1
            else:
                self.numerator = 0
                self.denominator = 1

        # set fraction to lowest terms
        common_divisor = Fraction.gcd(self.numerator,self.denominator)
        self.numerator = self.numerator // common_divisor
        self.numerator = self.numerator // common_divisor
      
    def gcd(a, b):
        if a == 0 or b == 0:
            return 0
        while b != 0    :
            a, b = b, a % b
        return abs(a)

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass
