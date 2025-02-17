def swap(list_one):
    """
    Function that swaps the first and last elements of the list, regardless of length
    :param list_one: a list of at least two elements
    :return: the same list with the first and last elements swapped
    """


fruit_switch = ["guava", "passion fruit", "lychee", "papaya"]
print(fruit_switch)
fruit_switch[0] = "papaya"
fruit_switch[3] = "guava"
print(fruit_switch)


def rotate_left(list_one):
    """
    Given a list of ints length 3, return a list with the elements "rotated left" so [1, 2, 3] yields [2, 3, 1].
    :param list_one: A list consisting of exactly three integers
    :return: a list where all the elements have been shifted 1 place to the left
    """


company_rotate = ["apple", "google", "microsoft"]
print(company_rotate)
company_rotate[0] = "google"
company_rotate[1] = "microsoft"
company_rotate[2] = "apple"
print(company_rotate)


def max_end(list_one):
    """
    This function will find if the first or last element of an list is larger, then set all the elements
    of that list to that value.
    :param list_one: A list consisting of three elements - all integers
    :return: A list where all the elements are the larger of the first or last element of the original list
    """



