def pent(n):
    """n-th pentagonal number"""
    return (3*n*n - n)//2


def is_pent(n):
    """is n a pentagonal number?"""
    if n <= 0:
        return False
    # Implement eq. (3)
    inv = (1+(24*n+1)**0.5)/6
    return inv == int(inv)


N, K = map(int, input().split())
out = set()

# Try everything up to max
for n in range(K+1, N):
    a, b = pent(n), pent(n-K)
    # Do we have a pent no.?
    if is_pent(a-b) or is_pent(a+b):
        out.add(a)
for x in sorted(out):
    print(x)
