#!/usr/bin/python3


def no_c(my_string):
    char_list = list(my_string)
    i = 0
    while i < len(char_list):
        if char_list[i] == 'C' or char_list[i] == 'c':
            char_list.pop(i)
        else:
            i += 1

    separator = ''
    result = separator.join(char_list)
    return result
