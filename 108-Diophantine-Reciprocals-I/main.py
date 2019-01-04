import random


def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while a:
        a, b = b % a, a
    return b


def brent(N):
    if N % 2 == 0:
        return 2
    y = random.randint(1, N - 1)
    c = random.randint(1, N - 1)
    m = random.randint(1, N - 1)
    g, r, q = 1, 1, 1
    while g == 1:
        x = y
        for i in range(r):
            y = ((y * y) % N + c) % N
        k = 0
        while k < r and g == 1:
            ys = y
            for i in range(min(m, r - k)):
                y = ((y * y) % N + c) % N
                q = q * (abs(x - y)) % N
            g = gcd(q, N)
            k = k + m
        r *= 2
    if g == N:
        while True:
            ys = ((ys * ys) % N + c) % N
            g = gcd(abs(x - ys), N)
            if g > 1:
                break
    return g


def primes(n):
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes


def try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True  # n is definitely composite


known_primes = primes(int(1e6))


def is_prime(n, precision=16):
    if n in known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    if n < 1373653:
        return not any(try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(try_composite(a, d, n, s)
                   for a in known_primes[:precision])


def factors(n):
    if n == 1:
        return {0: 0}
    if is_prime(n):
        return {n: 1}
    F = {}
    for p in known_primes:
        if n % p == 0:
            i = 0
            while n % p == 0:
                i += 1
                n //= p
            F[p] = i
        if n == 1:
            return F
    while n != 1:
        if is_prime(n):
            F[n] = 1
            break
        b = brent(n)
        i = 0
        while n % b == 0:
            i += 1
            n //= b
        F[b] = i
    return F


def ways(n):
    ans = 1
    for x in factors(n).values():
        ans *= 2*x+1
    ans = (1 + ans)//2
    return ans


T = int(input())
for _ in range(T):
    N = int(input())
    print(ways(N))
