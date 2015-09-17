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
