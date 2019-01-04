from math import ceil, log


def fib_dig(n):
    """First Fibonacci number with n digits"""
    # Implement eq. (6)
    PHI = (1 + 5**0.5)/2
    # Handle the one place our approximation fails
    if n == 1:
        return 1
    return ceil((n-1+log(5, 10)/2)/log(PHI, 10))


T = int(input())
for _ in range(T):
    N = int(input())
    print(fib_dig(N))
