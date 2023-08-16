#!/usr/bin/python3


def common_elements(set_1, set_2):
    common = []
    for val in set_1:
        if val in set_2:
            common.append(val)
    return set(common)
