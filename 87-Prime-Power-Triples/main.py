def bs(arr, l, r, x):
    """Binary Search arr from index l to r for x"""
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


# Create lists of valid prime powers
MAX = int(1e7)
P = primes(int(MAX**(1./2.)))
p2 = [p**2 for p in P]
p3 = [p**3 for p in P if p < MAX**(1./3.)]
p4 = [p**4 for p in P if p < MAX**(1./4.)]

# Keep unique sums
sums = set()
for a in p2:
    for b in p3:
        for c in p4:
            sums.add(a+b+c)
sums = list(sorted(sums))

T = int(input())
for _ in range(T):
    N = int(input())
    print(bs(sums, 0, len(sums)-1, N))
