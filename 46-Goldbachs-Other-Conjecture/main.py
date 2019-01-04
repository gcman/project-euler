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


# MAX input is 5*10^5
P = primes(int(5e5))


def ways(n):
    """No. of ways n can be written as p + 2k^2
    for prime p and integer k"""
    # Implement eq. (1)
    def cand(p): return ((n-p)/2)**0.5
    # Get no. of primes less than n which produce a valid candidate
    return len(set(p for p in P if p < n and cand(p) == int(cand(p))))


T = int(input())
for _ in range(T):
    N = int(input())
    print(ways(N))
