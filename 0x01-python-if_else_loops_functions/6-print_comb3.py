#!/usr/bin/python3
for i in range(0, 100):
    for j in range(0, 100):
        if i != j and i < j:
            print("{} {}, ".format(i, j), end="")
