class Fraction(object):
    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator,int) and isinstance(denominator,int):
            if denominator == 0:
                raise ZeroDivisionError("Denominator can't be zero")
            else:
                self.numerator = numerator
                self.denominator = denominator

        elif isinstance(numerator, str):
            fraction_str = numerator.strip()
            if '/' in fraction_str:
                numerator_str, denominator_str = fraction_str.split('/', 1)
                try:
                    self.numerator = int(numerator_str)
                    self.denominator = int(denominator_str)
                except ValueError:
                    self.numerator = 0
                    self.denominator = 1
            else:
                self.numerator = 0
                self.denominator = 1
        else:
            self.numerator = 0
            self.denominator = 1

        # ensure denominator is positive
        if self.denominator < 0:
            self.denominator *= -1
            self.numerator *= -1

        # set fraction to lowest terms
        common_divisor = Fraction.gcd(self.numerator,self.denominator)
        if common_divisor != 0:
            self.numerator = self.numerator // common_divisor
            self.denominator = self.denominator // common_divisor

    def gcd(a, b):
        if a == 0 or b == 0:
            return 0
        while b != 0:
            a, b = b, a % b
        return abs(a)

    def get_numerator(self):
        return str(self.numerator)

    def get_denominator(self):
        return str(self.denominator)

    def get_fraction(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return f"{self.numerator}/{self.denominator}"
