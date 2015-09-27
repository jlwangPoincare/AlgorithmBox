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
        for j in range(length_pattern):
            if instring[i + j] != pattern[j]:
                break
            #else:
                #pass
        else: # The loop ends normally
            return i
    else: # The outer loop ends normally, doesn't find the pattern
        return -1

# This looks good

print plain('incsearch', 'cso')
