def gcd(a, b):
"""
A function used to evaluate the greatest common divisor.
Input two integers, a and b. Do not need to be in order.
Program will check input types.
"""
    if not isinstance(a, int):
        print 'Noninteger input a'
        return None
    if not isinstance(b, int):
        print 'Noninteger input b'
        return None
    r = a % b
    if r == 0:
        return b
    return gcd(b, r)

