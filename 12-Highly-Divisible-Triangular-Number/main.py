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


P = primes(202)


def prime_factors(n):
    """Return the prime factorization of n"""
    factors = {}
    for p in P:
        if n % p == 0:
            factors[p] = 0
            while n % p == 0:
                n //= p
                factors[p] += 1
    return factors


# Memoize the latest num_of_factors
LATEST = [0, 0]


def factors(n):
    """Find the number of factors of n"""
    global LATEST
    if n == LATEST[0]:
        return LATEST[1]
    P = prime_factors(n)
    ans = 1
    for x in P:
        ans *= P[x] + 1
        LATEST = [n, ans]
    return ans


def triangle_factors(n):
    """Find the number of factors of T_n"""
    k = prime_factors((n//2 + n % 2) * 2)[2]
    return factors(n) * factors(n+1) * k // (k+1)


T = int(input())
for _ in range(T):
    N = int(input())
    i = 1
    while triangle_factors(i) <= N:
        i += 1
        print(i*(i+1)//2)
