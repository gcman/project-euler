def primes(n):
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2,n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite

# sum of first 379400 primes > 10^12
# 379400th prime is 5759059
_known_primes = primes(5759059)
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True

count = 0
prefix = [0]
for p in _known_primes:
    count += p
    prefix.append(count)

def longest_prime_sum(N):
    longest = [0,0]
    for i in range(longest[1],len(prefix)):
        for j in reversed(range(i-longest[1])):
            cand = prefix[i] - prefix[j]
            if cand > N:
                break
            if is_prime(cand) and i-j > longest[1]:
                longest = [cand,i-j]
    return longest[0],longest[1]

print(longest_prime_sum(1000000000000))
