from fractions import Fraction
print('Fraction(\'3.14159265359\') -> ',Fraction('3.14159265359'))
print('with limit_denominator(1000) -> ',Fraction('3.14159265359').limit_denominator(1000))
