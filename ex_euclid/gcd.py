def gcd(a, b):
"""
A function used to evaluate the greatest common divisor.
Input two integers, a and b. Do not need to be in order.
Program will check input types. Nonpositive input would
not work.
"""
    if not isinstance(a, int):
        print 'Noninteger input a'
        return None
    if not isinstance(b, int):
        print 'Noninteger input b'
        return None
    if a <= 0 or b <= 0:
        print 'Not positive integer inputted'
        return None

    # Key part
    r = a % b
    if r == 0:
        return b
    return gcd(b, r)
    # Key part end

