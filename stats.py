
# Mean function, length of number list will be determined using python's inbuilt length function,
# and the sum of all numbers will be determined using python's inbuilt sum function.
# Function will return calculated mean value.
def meanCalculation(numbers):
    listLength = len(numbers)
    summation = sum(numbers)
    mean = summation/listLength
    return mean
