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
        print a, '**', d, '=', temp, 'mod', n
        if temp == 1:
            # pass this a
            continue
        for r in range(s):
            temp = fast_int_mod_power(a, 2 ** r * d, n)
            print a, '** (', d, '* 2 **', r, ') =', temp, 'mod', n
            if temp == n-1:
                # Found, also pass this a
                break
        else:
            # End of for loop, not found any r s.t. a ** ( d * 2 ** r ) == n - 1
            print a, 'is a witness of', n
            print a, '**', d, '=', fast_int_mod_power(a, d, n), 'mod', n
            for r in range(s):
                print a, '** (', d, '* 2 **', r, ') =', fast_int_mod_power(a, 2 ** r * d, n), 'mod', n
            return a
        # break will jump here, continue this loop for next a

    #print 'Witness not found'
    return -1

def prime_test(n):
    if n < 2:
        return None
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    w = find_witness(n)
    if w > 0:
        print n, 'is not a prime number, with at least a witness:', w
        return False
    else:
        print n, 'is a prime number'
        return True

if __name__ == '__main__':
    
    while True:
        inp = int(raw_input('Please type in a number you want to test\n'))
        if inp != 0: 
            print prime_test(inp)
        else:
            break

    #find_witness(9937)
    #find_witness(5619)
    #find_witness(65537)
    #print fast_int_mod_power(2, 2808, 5619)
