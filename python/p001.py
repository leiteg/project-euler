#!/usr/bin/env python3
""" Project Euler - Problem 001

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def compute_answer():
    return sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)


if __name__ == '__main__':
    print(compute_answer())
