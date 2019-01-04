MOD = 10**9 + 7

def ways(k):
    ans = 1
    for i in range(1,10):
        ans *= k + i
    ans *= k + 20
    ans *= 283194722
    ans -= 10*k + 2
    ans %= MOD
    return ans

T = int(input())
for _ in range(T):
    print(ways(int(input())))
