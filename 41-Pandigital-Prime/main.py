from itertools import permutations
from math import sqrt


def bs(arr, l, r, x):
    """Binary Search arr from index l to r for x"""
    while l <= r:
        mid = l + (r - l)//2
        if arr[mid] == x:
            return arr[mid]
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
            return arr[r]


def primes(n):
    """Sieve of Eratosthenes"""
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            # Cross out all multiples of p
            for i in range(p * p, n + 1, p):
                sieve[i] = False
                return primes


def pandigital(n):
    """Find all n-digit pandigital numbers"""
    pan = "123456789"
    # Permute first n characters of pan
    out = permutations(pan[:n])
    # Join each tuple into a str, then an int
    return [int("".join(x)) for x in out]


# We need primes up to int(sqrt(10**7 - 1)) = 3162
P = primes(3162)
# All other pandigitals are divisible by 3
PAN = pandigital(4) + pandigital(7)
PAN_PRIME = []
for pan in PAN:
    # Test if pan is in our list of primes
    # Or it is not divisible by any prime <= sqrt(pan)
    if pan in P or all([pan % p != 0 for p in P if p <= int(sqrt(pan))]):
        PAN_PRIME.append(pan)

T = int(input())
for _ in range(T):
    N = int(input())
    print(bs(PAN_PRIME, 0, len(PAN_PRIME)-1, N))
