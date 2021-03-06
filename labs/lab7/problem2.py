# 2. Write two functions to check if a number is prime, and check which of them is more time-efficient.
import math


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True

    for i in range(3, number + 1):
        if number % i == 0:
            return False
    return True


def is_prime_optimized(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    max = int(math.sqrt(number))
    for i in range(3, max + 1):
        if number % i == 0:
            return False
    return True