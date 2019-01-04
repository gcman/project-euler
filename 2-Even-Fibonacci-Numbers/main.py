def next_even(f):
    """Implement eq. (5)"""
    return 4*f[1] + f[0]


def even_fib_sum(n):
    """Find the sum of even Fibonacci numbers up to n"""
    fib = [0, 2]  # Start with first two evens
    if n >= 2:
        count = 2
    else:
        count = 0
    # Go up to the maximum
    while next_even(fib) <= n:
        count += next_even(fib)
        # Keep track of last two evens
        fib = [fib[1], next_even(fib)]
    return count


T = int(input())
for _ in range(T):
    N = int(input())
    print(even_fib_sum(N))
