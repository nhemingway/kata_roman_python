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

    return _units(number)

def _units(number):
    if number <= 3:
        return 'I' * number
    elif number <= 5:
        return ('I' * (5 - number)) + 'V'
    elif number <= 8:
        return 'V' + ('I' * (number - 5))
    else:
        return ('I' * (10 - number)) + 'X'
