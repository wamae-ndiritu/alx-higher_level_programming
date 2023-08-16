#!/usr/bin/python3


def uniq_add(my_list=[]):
    result = 0
    uniq_integers = list(set(my_list))
    for val in uniq_integers:
        result += val
    return (result)
