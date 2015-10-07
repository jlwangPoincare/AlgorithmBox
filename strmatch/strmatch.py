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

#t1 = time.clock()
#print plain('abcabdabeabf' * 4 + 'abcabc', 'abcabc')
#print 'T1 = ', time.clock() - t1

def pre_process(a_string):
    """
    A function returning the characterized list of a pattern string.
    Trying to find the repetitive occurence of the prefix string.
    """
    # This is a test case
    #return [0, 0, 0, 0, 1, 2, 0]
    process_result = list()
    process_result.append(0);
    i = 2
    while i <= len(a_string):
        j = i - 1
        while j > 0:
            if a_string[:j] == a_string[i - j:i]:
                break
            j -= 1
        process_result.append(j)
        i += 1
    return process_result

def kmp_search(instring, pattern):
    """
    A function with basically the same behavior as plain. Search for
    the pattern string, return the index for the first time found.
    Use KMP algorithm, faster than plain.
    """
    partial_match_table = pre_process(pattern)
    length_instring = len(instring)
    length_pattern = len(pattern)
    i = 0
    j = 0
    while i < length_instring - length_pattern + 1:
        # search from instring[0] to instring[-length_pattern] for the pattern[0]
        # but i and j can be changed in the loop
        while j < length_pattern:
            # j starts from 0, if pattern[0] is not matched, break
            # i stays at the same position all the way, moves j only
            if instring[i + j] != pattern[j]:
                pass
                # modify i, j according to pattern_temp_list
                #i += j - partial_match_table[j-1] + 1
                #j = partial_match_table[j-1]
                #break
            j += 1
        else:
            # The loop ends normally, no break, which means the whole pattern is found
            return i
            # instring[i] == pattern[0], so return i
        # no need to add a break statement here
        #i += 1
    else:
        # The outer loop ends normally, pattern not found
        return -1
    # This is a mess

#print kmp_search('A ABCDAB ABCDABCDABDE', 'ABCDABD')
print pre_process('ABCDABD')


