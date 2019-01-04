from math import log


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


def min_mult(n):
    """Implement eq. (1)"""
    P = primes(n)
    ans = 1
    for p in P:
        ans *= p**int(log(n, p))
    return ans


T = int(input())
for _ in range(T):
    N = int(input())
    print(min_mult(N))
