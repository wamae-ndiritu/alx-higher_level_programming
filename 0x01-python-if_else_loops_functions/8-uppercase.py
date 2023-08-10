#!/usr/bin/python3


def uppercase(str):
    result = ""
    for c in str:
        if 'a' <= c <= 'z':
            upper_char = chr(ord(c) - ord('a') + ord('A'))
            result += "{}".format(upper_char)
        else:
            result += "{}".format(c)
    print(result)
