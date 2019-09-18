#!/usr/bin/env python3
""" Project Euler - Problem 004

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(s):
    return s == s[::-1]


def largest_palindrome(digits):
    assert digits >= 1
    low = 10**(digits - 1)
    high = 10**(digits)
    largest = 0
    for x in reversed(range(low, high)):
        for y in reversed(range(low, high)):
            s = str(x * y)
            if is_palindrome(s) and x * y > largest:
                largest = x * y
    return largest


def compute_answer():
    return largest_palindrome(digits=3)


if __name__ == '__main__':
    print(compute_answer())
