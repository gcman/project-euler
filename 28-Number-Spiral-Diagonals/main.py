def inv(a, m):
    """Modular inverse with Fermat's Little Theorem"""
    return pow(a, m-2, m)


def diag_sum(n, p):
    """Implement eq. (4), mod p"""
    return ((4*pow(n, 3, p) + 3*pow(n, 2, p) + 8*n - 9)*inv(6, p)) % p


T = int(input())
P = 1000000007
for _ in range(T):
    N = int(input())
    print(diag_sum(N, P))
