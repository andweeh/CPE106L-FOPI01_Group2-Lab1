#Programming Problem 1 - Mode Function
from collections import Counter

def modeCalculation(numbers):
    frequency = Counter(numbers)
    modes = frequency.most_common()
    max_count = modes[0][1]
    mode_list = []
    for mode in modes:
        if mode[1] == max_count:
            mode_list.append(mode[0])
        else:
            break
    return min(mode_list)

number_string = input("Enter a list of numbers separated by commas: ")
number_list = [int(num) for num in number_string.split(',')]
mode = modeCalculation(number_list)
print("The mode of the input list is: ", mode)

# Mean function, length of number list will be determined using python's inbuilt length function,
# and the sum of all numbers will be determined using python's inbuilt sum function.
# Function will return calculated mean value.
def meanCalculation(numbers):
    listLength = len(numbers)
    summation = sum(numbers)
    mean = summation/listLength
    return mean
