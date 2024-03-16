#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
nargs = len(argv)

print("{}".format(nargs), end=' ')
if nargs == 2:
    print("argument", end='')
else:
    print("arguments", end='')


if nargs == 1:
    print(".")
else:
    print(":")

for i in range(1, nargs):
    print("{}: {}".format(i, argv[i]))
