def inv(a, p):
    """Modular inverse with Fermat's Little Theorem"""
    return pow(a, p-2, p)


def choose(n, k, p):
    """n choose k mod p"""
    ans = 1
    # Recurrence in eq. (2)
    for i in range(k):
        ans = (ans * (n-i) * inv(i+1, p)) % p
    return ans


P = 1000000007
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(choose(N+M, min(N, M), P))
