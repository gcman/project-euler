def egcd(a, b):
    """Extended Euclidean Algorithm"""
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def inv(a, m):
    """Modular inverse"""
    g, x, y = egcd(a, m)
    if g != 1:
        return None
    else:
        return x % m


T = int(input())
for _ in range(T):
    a, b, N = map(int, input().split())
    k = inv(a, b)
    # Implement eq. (9)
    den = b*((N-k)//b) + k
    num = (a*den - 1)//b
    print(num, den)
