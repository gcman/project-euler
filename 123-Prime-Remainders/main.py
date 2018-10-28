def primes(n):
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes

def bs(arr, l, r, x):
    while l <= r:
        mid = l + (r - l)//2;
        if arr[mid] == x:
            return mid + 1
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return r + 1

P = primes(3500000)
rem = [2*(i+1)*P[i] % P[i]**2 for i in range(0,len(P)-1,2)]

T = int(input())
for _ in range(T):
    N = int(input())
    if N == 1:
        print(2)
    else:
        ans = 2*bs(rem,0,len(rem)-1,N) + 1
        print(ans)
