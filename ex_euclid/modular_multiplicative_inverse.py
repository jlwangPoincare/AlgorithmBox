import ex_euclid

def modular_multiplicative_inverse(element, modulous):
    (temp1, temp_d, temp3) = ex_euclid.ex_euclid(modulous, element)
    if temp_d * element % modulous != 1:
        print 'd failed'
        return None
    return temp_d

#modular_multiplicative_inverse(7, 10)
