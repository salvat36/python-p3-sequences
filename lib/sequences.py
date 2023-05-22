#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = []
    if length > 0:
        sequence.append(0)
    if length > 1:
        sequence.append(1)
    if length >= 3:
        for i in range (length - 2):
            sequence.append(sequence[-1] + sequence[-2])
    print(sequence)
    return sequence





    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,