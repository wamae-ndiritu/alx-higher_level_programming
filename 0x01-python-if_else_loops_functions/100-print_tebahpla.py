#!/usr/bin/python3

for c in range(ord('z'), ord('a') - 1, -1):
    if (ord('z') - c) % 2 == 0:
        print("{:c}".format(c), end="")
    else:
        print("{:c}".format(c - (ord('a') - ord('A'))), end="")
