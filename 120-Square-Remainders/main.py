MOD = 1000000007


def s(a, e):
    if a <= 1:
        return 0
    if e == 2:
        if a == 2:
            return 2
        b = (a-1)//2
        ans = b*(b+1)*(8*b+13)//6
        if a % 2 == 1:
            ans -= 2*b*(b+1)
        return (2+2*ans) % MOD
    elif e == 3:
        if a == 2:
            return 4
        return (4 + a*(a+1)*(3*a**2-a-2)//12) % MOD


for a in range(1, 100):
    print(a, sorted([(i, 2+n*(n-1)*a**2 % a**3)
                     for i, n in enumerate(range(a))], key=lambda x: x[1])[-1])
