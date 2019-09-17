#!/usr/bin/env python3
""" Project Euler - Problem 003

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

from library import memoize
from math import sqrt


@memoize
def factors(number):
    factors = [1, number]
    pos = 1
    for i in range(2, int(sqrt(number)) + 1):
        div, rem = divmod(number, i)
        if rem == 0:
            factors.insert(pos, i)
            if i != div:
                factors.insert(-pos, div)
            pos += 1
        if i >= div:
            break
    return factors


def is_prime(number):
    return len(factors(number)) == 2


def prime_factors(number):
    return (x for x in factors(number) if is_prime(x))


def compute_answer():
    return max(prime_factors(600851475143))


if __name__ == '__main__':
    print(compute_answer())
