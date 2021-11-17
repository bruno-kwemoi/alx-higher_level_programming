#!/usr/bin/python3
def print_last_digit(number):
    last = abs(number)
    print(last % 10, end="")
    return(last % 10)
