def triangular(n):
    """Implement eq. (1)"""
    return n * (n+1) // 2


def sum_under(n, m):
    """Terms in eq. (3)"""
    return m*triangular((n-1)//m)


T = int(input())
for _ in range(T):
    N = int(input())
    print(sum_under(N, 3) + sum_under(N, 5) - sum_under(N, 15))
