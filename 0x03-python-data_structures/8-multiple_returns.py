#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    char = sentence
    char = sentence[0] if length > 0 else None
    tuple = (len(sentence), char)
    return(tuple)
