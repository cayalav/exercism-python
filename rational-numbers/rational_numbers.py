from __future__ import division


def greatest_common_divisor(first, second):

    first_factors = factors(abs(first))

    second_factors = list(factors(abs(second)))

    return next(
        (f for f in first_factors if f in second_factors), 1)


def factors(number):
    return (x for x in range(number, 0, -1) if number % x == 0)


class Rational(object):

    def __init__(self, numerator, denominator):
      
        gcd = greatest_common_divisor(numerator, denominator)


        sign = denominator / abs(denominator)

        self.numerator = int(sign * numerator / gcd)
        if numerator == 0:
            self.denominator = 1
        else:
            self.denominator = int(sign * denominator / gcd)

    def __eq__(self, other):
        same_numerator = self.numerator == other.numerator
        same_denominator = self.denominator == other.denominator
        return same_numerator and same_denominator

    def __repr__(self):
        return '{}/{}'.format(self.numerator, self.denominator)

    def __add__(self, other):
        return Rational(
            self.numerator * other.denominator +
            other.numerator * self.denominator,
            self.denominator * other.denominator)

    def __sub__(self, other):
        return Rational(
            self.numerator * other.denominator -
            other.numerator * self.denominator,
            self.denominator * other.denominator)

    def __mul__(self, other):
        return Rational(
            self.numerator * other.numerator,
            self.denominator * other.denominator)

    def __truediv__(self, other):
        return Rational(
            self.numerator * other.denominator,
            self.denominator * other.numerator)

    def __abs__(self):
        return Rational(abs(self.numerator), self.denominator)

    def __pow__(self, power):
        return Rational(
            self.numerator ** power, self.denominator ** power)

    def __rpow__(self, base):
        return base ** (self.numerator / self.denominator)