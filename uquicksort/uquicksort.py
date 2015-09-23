def uqsort(given_list, reverse = False):
    """
    Take a given list and quick sort it, return a new, sorted list.
    Defause sort as ascending, if reverse is set as True, sort descending.
    """
    #I think Python has list.sort() method as quick sort. Whatever, I
    #need to write it myself.
    if len(given_list) <= 1:
        return given_list
    if reverse:
        pass
    pivot_value = given_list[0]
    iter1 = 0
    iter2 = len(given_list) - 1
    pivot_buffer = 0
    while iter1 < iter2:
        if given_list[iter2] < given_list[iter1]:
            given_list[iter1] = given_list[iter2]
            pivot_buffer = iter2
            iter1 += 1
        elif 
    #Something like this...


sample_list = ['s', 'a', 'd', 'l', 'e', 'r', 'n', 'z', 't', 'b']
print sample_list
print 'Python sort: ', sample_list.sort()
#print uqsort(sample_list)
