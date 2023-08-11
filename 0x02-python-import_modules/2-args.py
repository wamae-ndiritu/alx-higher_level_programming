#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    args = sys.argv[1:]

    print("{} argument{}{}"
          .format(argc, "s" if argc != 1 else "", "."
                  if argc == 0 else ":"), end="")
    if argc > 0:
        print()
        for i, arg in enumerate(args, start=1):
            print("{:d}: {}".format(i, arg))
    else:
        print()
