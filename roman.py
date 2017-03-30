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

    thousands = number / 1000 % 10
    hundreds = number / 100 % 10
    tens = number / 10 % 10
    units = number % 10
    #print "Tens: %d, Units: %d" % (tens, units)
    return _thousands(thousands) + _hundreds(hundreds) + _tens(tens) + _units(units)

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

def _hundreds(digit):
    return _digit(digit, 'C', 'D', 'M')

def _thousands(digit):
    if digit >= 4:
        raise ValueError('Too large')
    
    return _digit(digit, 'M', '#', '#')
