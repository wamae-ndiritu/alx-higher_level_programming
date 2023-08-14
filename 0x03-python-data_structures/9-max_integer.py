#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    for i in range(len(my_list)):
        for j in range(len(my_list) - i - 1):
            if my_list[j] > my_list[j + 1]:
                temp_element = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp_element
    max_int = my_list[len(my_list) - 1]
    return max_int
