# 1		I
# 2		II
# 4		IV
# 5		V
# 10		X
# 50		L
# 100	C
# 500	D
# 1000	M

def roman(number):
    if number < 1:
        raise ValueError('Number must be strictly positive')

    return 'I'
