def next_convergent(p, q):
    """Implement eq. (2)"""
    return p+2*q, p+q


p, q = 1, 1
N = int(input())
for i in range(1, N+1):
    p, q = next_convergent(p, q)
    # Does num have more digits than den?
    if len(str(p)) > len(str(q)):
        print(i)
