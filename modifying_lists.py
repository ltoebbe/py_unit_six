
def create_list(starting, ending):
    """
    Ex. create_list(4, 10) would return [4, 5, 6, 7, 8, 9, 10]
    :param starting: an integer number
    :param ending: A number greater than the starting number
    :return: list of numbers starting with the first number and going up to and including the second number
    """
    length = ending - starting
    list = [1]
    list[0] = starting
    for x in range(length):
        list.append(int(list[-1] + 1))
    return list


print(create_list(1, 20))

def find_odds(numbers):
    """
    Ex. find_odds([13, 2, 9, 14, 16, 18, 9, 11, 21]) would return [13, 9, 9, 11, 21]
    :param numbers: a list of numbers
    :return: a new list consisting of only the odd numbers from the original list
    """
    numbers = [13, 2, 9, 14, 16, 18, 9, 11, 21]
    if list() % 2 = 1:


print(find_odds())


def remove_duplicates(numbers):
    """
    Ex. remove_duplicates([1, 2, 3, 3, 4, 5, 6, 6, 7, 7, 7])  would return  [1, 2, 3, 4, 5, 6, 7]
    remove_duplicates9[‘apple’, ‘banana’, ‘banana’, ‘cherry’]) would return [‘apple’, ‘banana’, ‘cherry’]
    :param numbers:
    :return:
    """

    pass # remove this line when starting your function
