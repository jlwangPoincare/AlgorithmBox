import time
def plain(instring, pattern):
    """
    A function uses plain string searching algorithm.
    Input a string, and a pattern to be searched.
    Return the index where the whole pattern is found for the first time.
    If pattern not found, return -1.
    """
    length_instring = len(instring)
    length_pattern = len(pattern)
    for i in range(length_instring - length_pattern + 1):
        # search from instring[0] to instring[-length_pattern] for the pattern[0]
        for j in range(length_pattern):
            # j starts from 0, if pattern[0] is not matched, break
            # i stays at the same position all the way, moves j only
            if instring[i + j] != pattern[j]:
                break
        else:
            # The loop ends normally, no break, which means the whole pattern is found
            return i
            # instring[i] == pattern[0], so return i
        # no need to add a break statement here
    else:
        # The outer loop ends normally, pattern not found
        return -1
    # In this program, for-else statements are useful

# In plain match algorithm, every time the position where the pattern match start in
# the instring increse by 1. As the index in patter, the index in instring may go
# back, thus it's not very convenient to use i to indicate the character to be
# compared in instring.

#t1 = time.clock()
#print plain('abcabdabeabf' * 4 + 'abcabc', 'abcabc')
#print 'T1 = ', time.clock() - t1

def pre_process(pattern):
    """
    A function returning the characterized list of a pattern string.
    Trying to find the repetitive occurence of the prefix string.
    """
    # In the 'next' array, nxt_table[j] is the index j should go to
    # when instring[i] != pattern[j]
    length_pattern = len(pattern)
    nxt_table = list()
    nxt_table.append(-1)
    j = 0
    # j points to the position in the pattern string
    k = -1
    # k points to the position in a substring
    while j < length_pattern - 1:
        if k == -1 or pattern[j] == pattern[k]:
            k += 1
            j += 1
            l = k
            if l != -1 and pattern[j] == pattern[l]:
                l = nxt_table[l]
            nxt_table.append(l)
            # nxt_table[j] = l (nxt_table[j] is nxt_table[j+1] previously to j += 1)
        else:
            k = nxt_table[k]
    return nxt_table

    # Initialize the 0th element in nxt as -1

    # In this version, pre_process is not the best
    #process_result = list()
    #process_result.append(0);
    #i = 2
    #while i <= len(pattern):
        #j = i - 1
        #while j > 0:
            #if pattern[:j] == pattern[i - j:i]:
                #break
            #j -= 1
        #process_result.append(j)
        #i += 1
    #print process_result
    #return process_result

def kmp_search(instring, pattern):
    """
    A function with basically the same behavior as plain. Search for
    the pattern string, return the index for the first time found.
    Use KMP algorithm, faster than plain.
    """
    nxt = pre_process(pattern)
    length_instring = len(instring)
    length_pattern = len(pattern)
    i = 0
    #i points to the character to be matched in instring
    j = 0
    #j points to the character to be matched in pattern
    while i < length_instring:
        if j == -1 or instring[i] == pattern[j]:
            i += 1
            j += 1
            if j == length_pattern:
                return i - j + 1
        else:
            j = nxt[j]
    return -1
    # End while

# In KMP algorithm, the index in instring can never decrease. Thus it is
# convenient to use i to indicate the character to compare in instring.

#print pre_process('ABACABABA')
#print kmp_search('A ABCDAB ABCDABCDABDE', 'ABCDABD')


