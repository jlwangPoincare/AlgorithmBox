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

#print plain('incsearch', 'cso')

def kmp_search(instring, pattern):
    pass
