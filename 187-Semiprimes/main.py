# Binary search
def bs(arr, l, r, x):
    while l <= r:
        mid = l + (r - l)//2
        if arr[mid] == x:
            return mid + 1
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return r + 1


def primes(n):
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes


LIMIT = 10**8
PRIMES = primes(LIMIT//2)
S = sum([max(0, bs(PRIMES, 0, len(PRIMES)-1, LIMIT//p)-i)
         for i, p in enumerate(PRIMES)])
print(S)
