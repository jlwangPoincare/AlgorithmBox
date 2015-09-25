import random
import time

def basic_quicksort(given_list):
    """
    Take a given list and quick sort it, return a new, sorted list in ascending form.
    """
    if len(given_list) <= 1:
        # Base case
        return given_list
    pivot_value = given_list[0]
    iter1 = 0
    iter2 = len(given_list) - 1
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
    return uqsort(given_list[:pivot_buffer]) + [pivot_value] + uqsort(given_list[pivot_buffer + 1:])

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
    if reverse:
        pivot_value = given_list[0]
        iter1 = 0
        iter2 = len(given_list) - 1
        pivot_buffer = 0
        while iter1 < iter2:
            while iter1 < iter2 and pivot_buffer == iter1:
                if given_list[iter2] <= pivot_value:
                    iter2 -= 1
                else:
                    given_list[pivot_buffer] = given_list[iter2]
                    pivot_buffer = iter2
                    iter1 += 1
            while iter1 < iter2 and pivot_buffer == iter2:
                if given_list[iter1] >= pivot_value:
                    iter1 += 1
                else:
                    given_list[pivot_buffer] = given_list[iter1]
                    pivot_buffer = iter1
                    iter2 -= 1
        return uqsort(given_list[:pivot_buffer]) + [pivot_value] + uqsort(given_list[pivot_buffer + 1:])
    #This is the case of reverse == True
    return basic_quicksort(given_list)

if __name__ == '__main__':
    print 'Generate a random list with 10 million random integers'
    t0 = time.clock()
    random_list = []
    for i in range(10000000):
        random_list.append(random.randint(1,100000000))
    print 'Time 0: ', time.clock() - t0

    random_copy = random_list[:]
    print 'Sort random list with built-in sort method'
    t1 = time.clock()
    random_list.sort()
    print 'Time 1: ', time.clock() - t1

    print 'Sort random list with user-defined function'
    t2 = time.clock()
    random_copy = uqsort(random_copy)
    print 'Time 2: ', time.clock() - t2

    # This test shows built-in list.sort() works much better
