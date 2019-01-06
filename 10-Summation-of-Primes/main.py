def bs(arr, l, r, x):
    """Binary Search arr from index l to r for x"""
    while l <= r:
        mid = l + (r - l)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return r


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


PRIMES = primes(int(2e6))
# Construct the prefix sum array
P = [0]
count = 0
for p in PRIMES:
    count += p
    P.append(count)
del P[0]

T = int(input())
for _ in range(T):
    N = int(input())
    idx = bs(PRIMES, 0, len(PRIMES)-1, N)
    print(P[idx])
