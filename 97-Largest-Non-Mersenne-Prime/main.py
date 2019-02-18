MOD = pow(10, 12)


def modsum(a, b, c, d):
    return ((a*pow(b, c, MOD)) % MOD + d) % MOD


S = 0
T = int(input())
for _ in range(T):
    A, B, C, D = map(int, input().split())
    S = (S + modsum(A, B, C, D)) % MOD

# Pad the answer with leading zeroes
S = "".join(["0" for _ in range(12 - len(str(S)))]) + str(S)
print(S)
