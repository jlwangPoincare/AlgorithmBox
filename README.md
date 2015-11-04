AlgorithmBox
============================================================
    
Store some of my implementation of good algorithms here.

Categories
------------------------------------------------------------

### ex_euclid: An implementation of extended Euclidean algorithm
*This module originally was designed for implementing RSA algorithm*

    ex_euclid.py A module containing several related functions
    ex_euclid.gcd() A function calculates the greatest common divisor
    ex_euclid.ex_euclid() A function of extended Euclidean algorithm, which calculates x and y enables ax + by = gcd(a,b)
    ex_euclid.m_inverse() A function calculates the modulous inverse of a number e with modulous n

### uquicksort: An implementation of quick sort algorithm
    uquicksort.py A module containing quick sort function
    uquicksort.basic_quicksort() A function taking a list as argument, returning the sorted list
    uquicksort.uqsort() A function taking a list as argument, returning the sorted list, with option of ascending or descending

### strmatch: Several algorithms for string search
    strmatch.py A module containing functions for string search (or called substring matching)
    strmatch.plain() Plain string search
    strmatch.kmp_search() KMP string search algorithm, with good next array
    strmatch.pre_process() Function generating next array for KMP algorithm

### prime_test
    prime_test.py A module containing useful functions for Miller-Rabin primality testing algorithm
    prime_test.prime_test() Miller-Rabin primality testing function, take an integer as input
    prime_test.find_witness() Find the least witness (starting from 2) in Miller-Rabin algorithm of input
    prime_test.fast_ind_mod_power() The fastest way to do integer power calculation (with mod n)

### graph
    graph.py A class implementation of graph theory algorithms
