def omega(n):
    """No. of distinct prime factors of all m < n"""
    sieve = [0] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p] == 0:
            for i in range(p, n + 1, p):
                sieve[i] += 1
    return sieve

# Find all consec. sets of size k
# k distinct prime factors each


def consecutive(n, k):
    """Find all consec. sets of size k where
    each element has exactly k distinct prime factors"""
    FACTORS = omega(n+k-1)
    out = []
    for i in range(n+1):
        if all([FACTORS[i+j] == k for j in range(k)]):
            out.append(i)
    return out


N, K = map(int, input().split())
for x in consecutive(N, K):
    print(x)
