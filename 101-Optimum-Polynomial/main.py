def egcd(a, b):
    """Extended Euclidean Algorithm"""
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    """Multiplicative inverse of a mod m"""
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist!')
    else:
        return x % m


def prod(arr, M):
    out = 1
    for x in arr:
        out = out * x % M
    return out


def P(x, M):
    """Evaluate P at x mod M"""
    out = 0
    for i, coeff in enumerate(coeffs):
        out = (out + coeff*pow(x, i, M)) % M
    return out


def lagrange(x, n, M):
    out = 0
    for i in range(n):
        nums = [(x-j-1) for j in range(n) if i != j]
        dens = [(i-j) for j in range(n) if i != j]
        out = (out + seq[i]*prod(nums, M)*modinv(prod(dens, M), M)) % M
    return out % M


MOD = 1000000007
N = int(input())
coeffs = [x % MOD for x in list(map(int, input().split()))]
seq = [P(i+1, MOD) for i, x in enumerate(coeffs)]

S = [lagrange(n+1, n, MOD) for n in range(1, N+1)]
print(*S)
