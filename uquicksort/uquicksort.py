def uqsort(given_list, reverse = False):
    """
    Take a given list and quick sort it, return a new, sorted list.
    Default sort as ascending, if reverse is set as True, sort descending.
    """
    #I think Python has list.sort() method as quick sort. Whatever, I
    #need to write it myself.
    if len(given_list) <= 1:
        # Base case
        return given_list
    #if reverse:
        #pass
    #This is the case of reverse == True
    pivot_value = given_list[0]
    iter1 = 0
    iter2 = len(given_list) - 1
    #iter1 and iter2 should have no problem
    pivot_buffer = 0
    while iter1 < iter2:
        while iter1 < iter2 and pivot_buffer == iter1:
            if given_list[iter2] >= pivot_value:
                iter2 -= 1
            else:
                given_list[pivot_buffer] = given_list[iter2]
                pivot_buffer = iter2
                iter1 += 1
        while iter1 < iter2 and pivot_buffer == iter2:
            if given_list[iter1] <= pivot_value:
                iter1 += 1
            else:
                given_list[pivot_buffer] = given_list[iter1]
                pivot_buffer = iter1
                iter2 -= 1
    if pivot_buffer == len(given_list):
        return uqsort(given_list[:pivot_buffer]) + [pivot_value]
    return uqsort(given_list[:pivot_buffer]) + [pivot_value] + uqsort(given_list[pivot_buffer + 1:])
# Seems right from me

sample_list = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o']
sample_copy = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o']
print sample_list
sample_list.sort()
print 'Python sort: ', sample_list
print 'User sort:   ', uqsort(sample_copy)
