#!/usr/bin/python3


def uppercase(str):
    for c in str:
        if 'a' <= c <= 'z':
            upper_char = chr(ord(c) - ord('a') + ord('A'))
            print("{}".format(upper_char), end="")
        else:
            print("{}".format(c), end="")
    print()
