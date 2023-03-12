def mode(numbers):
    count_dict = {}
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    max_count = max(count_dict.values())
    mode_list = [k for k, v in count_dict.items() if v == max_count]
    return mode_list[0]

# Mean function, length of number list will be determined using python's inbuilt length function,
# and the sum of all numbers will be determined using python's inbuilt sum function.
# Function will return calculated mean value.
def meanCalculation(numbers):
    listLength = len(numbers)
    summation = sum(numbers)
    mean = summation/listLength
    return mean
