# 1	I
# 5	V
# 10	X
# 50	L
# 100	C
# 500	D
# 1000	M

def roman(number):
    if number < 1:
        raise ValueError('Number must be strictly positive')

    tens = number / 10 % 10
    units = number % 10
    #print "Tens: %d, Units: %d" % (tens, units)
    return _tens(tens) + _units(units)

def _digit(digit, one, five, ten):
    if digit == 0:
        return ''
    elif digit <= 3:
        return one * digit
    elif digit <= 5:
        return (one * (5 - digit)) + five
    elif digit <= 8:
        return five + (one * (digit - 5))
    elif digit < 10:
        return (one * (10 - digit)) + ten
    else:
        raise LogicError('Digit %d greater than 10' % digit)

def _units(digit):
    return _digit(digit, 'I', 'V', 'X')

def _tens(digit):
    return _digit(digit, 'X', 'L', 'C')
