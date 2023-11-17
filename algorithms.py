nums_to_sum = [9, 5, 11, 6, 1, 15]


def add_numbers(nums_to_sum):
    """
    Ex. add_numbers([9, 5, 11, 6, 1, 15]) returns 47
    :param nums_to_sum: a list of numbers
    :return: the sum of all the numbers in the list
    """
    summed_nums = 0
    for sum_of_nums in range(len(nums_to_sum)):
        summed_nums = nums_to_sum[0] + summed_nums
        del nums_to_sum[0]
    return summed_nums


print(add_numbers(nums_to_sum))


# ________________________________________________________________________________________________

list2minmax = [45, 23, 99, 34, 67, 98, 0]


def get_max(list2minmax):
    """
    Ex. get_max([45, 23, 99, 34, 67, 98, 0]) returns 99
    :param list2minmax: a list of numbers
    :return: The largest number in the list
    """
    for x in range(len(list2minmax) - 1):
        if list2minmax[0] > list2minmax[1]:
            del list2minmax[1]
        elif list2minmax[0] < list2minmax[1]:
            del list2minmax[0]
    return list2minmax


get_max(list2minmax)
print(get_max(list2minmax))

# ________________________________________________________________________________________________

list2minmax = [45, 23, 99, 34, 67, 98, 0]


def get_min(numbers):
    """
    Ex. get_min([45, 23, 99, 34, 67, 98, 0]) returns 0
    :param numbers: a list of numbers
    :return: The smallest number in the list
    """
    for x in range(len(list2minmax) - 1):
        if list2minmax[0] < list2minmax[1]:
            del list2minmax[1]
        elif list2minmax[0] > list2minmax[1]:
            del list2minmax[0]
    return list2minmax


get_min(list2minmax)
print(get_min(list2minmax))


# ________________________________________________________________________________________________

list1 = [3, 4, 7, 9]
list2 = [1, 5, 8, 11]


def merge(list1, list2):
    """
    Ex. merge([3, 4, 7, 9], [1, 5, 8, 11]) return [1, 3, 4, 5, 7, 8, 9, 11]
    :param list1: a list in sorted order
    :param list2: a second list in sorted order
    :return: a single list consisting of both smaller lists combined in sorted order.
    """
    list.sort(list1)
    print(list1)
