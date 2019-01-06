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


def n_primes(n):
    """Generate more than n primes with eq. (1)"""
    upper = int(n*log(n) + n*log(log(n)))
    return primes(upper)


P = n_primes(10001)
T = int(input())
for _ in range(T):
    N = int(input())
    print(P[N-1])
