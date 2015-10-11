# This file can be used as a module to be imported
# Type "import ex_euclid"

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

def ex_euclid(a1, b1):
    """
    A function used to implement the extended Euclidean algorithm.
    Input two positive integers, a1 and b1. Same as gcd(), do not
    need to be in order. Program will check input types.
    """
    if not isinstance(a1, int):
        print 'Noninteger input a'
        return None
    if not isinstance(b1, int):
        print 'Noninteger input b'
        return None
    if a1 <= 0 or b1 <= 0:
        print 'Not positive integer inputted'
        return None

    # Key part
    q1, r1 = divmod(a1, b1) # Tuple-returning function
    if r1 == 0:
        # Returned value are X1, Y1 and g that satisfy a1*X1 + b1*Y1 = g, and g is gcd
        return (0, 1, b1) # X1 = 0, Y1 = 1, g = b1, since a1 % b1 = 0, b1 = g
    tx1 = 1
    ty1 = -q1
    # a1*tx1 + b1*ty1 = r1, b1 is a2, r1 is b2
    # ex_euclid should return X2 and Y2 that satisfy b1*X2 + r1*Y2 = g
    # and r1 = a1*tx1 + b1*ty1, so a1*tx1*Y2 + b1*X2 + b1*ty1*Y2 = g
    (X2, Y2, g) = ex_euclid(b1, r1)
    X1 = tx1 * Y2
    Y1 = ty1 * Y2 + X2
    return (X1, Y1, g)
    # Key part end

def m_inverse(element, modulous):
    """
    A function used to calculate the modular multiplicative inverse.
    Using the extended Euclidean algorithm.
    """
    if not isinstance(element, int):
        print 'Noninteger input element'
        return None
    if not isinstance(modulous, int):
        print 'Noninteger input modulous'
        return None
    if element >= modulous or modulous <= 0:
        print 'Bad integer inputted'
        return None

    # Key part
    (temp1, temp_d, temp3) = ex_euclid(modulous, element)
    if not (temp_d >= 0 and temp_d < modulous):
        temp_d -= temp_d / abs(temp_d) * modulous
    # Make sure returned d is between 0 and modulous - 1. temp_d / abs(temp_d) is a sign
    if temp_d * element % modulous != 1:
        print 'd failed'
        return None
    return temp_d
    # Key part end

if __name__ = '__main__':
    # Put your code as the main function here
    # Won't be executed when used as imported package
