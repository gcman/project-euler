def prod(arr, m):
    """Multiply an array mod m"""
    out = 1
    for x in arr:
        out = out * x % m
    return out


def P(coeffs, x, m):
    """Evaluate P (given by its coefficients) at x mod m"""
    out = 0
    for i, coeff in enumerate(coeffs):
        out = (out + coeff*pow(x, i, m)) % m
    return out


def next_row(row, m):
    """Given a row of Pascal's triangle, gives the next mod m"""
    out = [(row[i] + row[i+1]) % m for i in range(len(row)-1)]
    return [1] + out + [1]


def fit(N, m):
    """Implement eq. (8) to find the first N FITs"""
    curr_row = [1]
    FIT = []
    for n in range(1, N+1):
        # this is L_n from eq. (8)
        curr_row = next_row(curr_row, m)
        next_fit = sum([pow(-1, (n-i) % 2)*curr_row[i-1]*seq[i-1]
                        for i in range(1, n+1)]) % m
        FIT.append(next_fit)
    return FIT


MOD = 1000000007
N = int(input())
COEFFS = [x % MOD for x in list(map(int, input().split()))]
seq = [P(i+1, MOD) for i, x in enumerate(COEFFS)]

print(*fit(N, MOD))
