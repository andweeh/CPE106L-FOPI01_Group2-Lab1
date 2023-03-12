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
