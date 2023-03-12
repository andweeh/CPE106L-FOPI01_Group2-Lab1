#<<<<<<< raphael_light
def median(list):
    """
    Author: Liwanag, John Rafael L.
    Takes as a sorted list of numbers as an argument 
    and returns the median.
    """
    n = len(list)
    if(n % 2 == 0):
        median = (list[int(n/2)] + list[int((n/2)-1)])/2
    else:
        median = list[int(n/2)]
    return median
#=======
#Programming Problem 1 - Mode Function
from collections import Counter

def mode(numbers):
    frequency = Counter(numbers)
    modes = frequency.most_common()
    max_count = modes[0][1]
    mode_list = []
    for mode in modes:
        if mode[1] == max_count:
            mode_list.append(mode[0])
        else:
            break
    return mode_list

# Mean function, length of number list will be determined using python's inbuilt length function,
# and the sum of all numbers will be determined using python's inbuilt sum function.
# Function will return calculated mean value.
def mean(numbers):
    listLength = len(numbers)
    summation = sum(numbers)
    mean = summation/listLength
    return mean
#>>>>>>> main
