#!/usr/bin/python3
"""
module function that prints text
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    list_lines = [lines.strip(' ') for lines in text.split('\n')]
    revised = "\n".join(list_lines)
    print(revised, end="")
