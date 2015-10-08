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
    # In this version, pre_process is not the best
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
    next_table = pre_process(pattern)
    length_instring = len(instring)
    length_pattern = len(pattern)
    i = 0
    #i points to the character to be matched in instring
    j = 0
    #j points to the character to be matched in pattern
    while i < length_instring:
        while j > 0 and instring[i] != pattern[j]:
            # This while deal with when part of pattern is matched and j not matched
            # Only in this case, i don't move
            # move j to a matched position in the previous part or move j to 0
            j = next_table[j - 1]
            # next_table[j-1] stores the position where pattern string can
            # match itself
        if instring[i] == pattern[j]:
            # This if distinguishs j == 0 from i j matched
            # Whatever, i will move. j will move if matched
            j += 1
        if j == length_pattern:
            # If after j move, j at the end of pattern, means whole pattern matched
            return i - j + 1
            # Calculate the index of the first match position
        i += 1
    return -1
    # If the loop ends, no match found
    # End while

print pre_process('ABCDABD')
print kmp_search('A ABCDAB ABCDABCDABDE', 'ABCDABD')


