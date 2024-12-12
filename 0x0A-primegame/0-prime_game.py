#!/usr/bin/python3
"""
Prime Game module.
Maria and Ben play a game where they pick prime
numbers and remove them and their multiples
from a set of consecutive integers. The player who cannot make a move loses.
"""


def is_prime(num):
    """Check if a number is a prime number."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def sieve_of_eratosthenes(max_num):
    """Generate a list of prime numbers up to
      max_num using the Sieve of Eratosthenes."""
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False
    return [i for i, is_prime in enumerate(primes) if is_prime]


def isWinner(x, nums):
    """Determine the winner of the game."""
    if not nums or x <= 0:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    prime_counts = [0] * (max_n + 1)

    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if i in primes else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
