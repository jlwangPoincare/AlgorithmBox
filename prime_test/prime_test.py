# Miller-Rabin algorithm

def fast_int_mod_power(base, exponent, n):
    inbase2 = list()
    basepowers = list()
    while(exponent > 0):
        exponent, r = divmod(exponent, 2)
        inbase2.append(r)
        basepowers.append(base)
        base = base * base % n
    result = 1
    for i in range(len(inbase2)):
        #print 'base ** (2 **', i, ') = ', basepowers[i]
        if inbase2[i] == 1:
            #print 'result = ', result, ' * ',  basepowers[i], ' = ',
            result = result * basepowers[i] % n
            #print result
    return result

def find_max_2(n):
    n_1 = n - 1
    counter = 0
    while n_1 % 2 == 0:
        counter += 1
        n_1 /= 2
    #print 'input n = ', n
    #print 'n - 1 = ', n_1, ' * (2 ** ', counter, ')'

    return n_1, counter

def find_witness(n):
    (d, s) = find_max_2(n)
    print 'd = ', d, 's = ', s
    for a in range(2, n-2):
        temp = fast_int_mod_power(a, d, n)
        if temp == 1:
            # pass this a
            continue
        for r in range(s):
            temp = fast_int_mod_power(a, 2 ** r * d, n)
            if temp == n-1:
                # Found, also pass this a
                break
                #print a, 'is a witness of', n
                #print a, '** (', d, '* 2 **', r, ') != -1 mod', n
                #print a, '** (', d, '* 2 **', r, ') =', temp, 'mod', n
                #return a
        else:
            # End of for loop, not found any r s.t. a ** ( d * 2 ** r ) == n - 1
            print a, 'is a witness of', n
            print a, '**', d, '=', fast_int_mod_power(a, d, n), 'mod', n
            for r in range(s):
                print a, '** (', d, '* 2 **', r, ') =', fast_int_mod_power(a, 2 ** r * d, n), 'mod', n
            return a
        # break will jump here, continue this loop for next a

    print 'Witness not found'
    return -1


find_witness(9937)
find_witness(5619)
find_witness(65537)
print fast_int_mod_power(2, 2808, 5619)
