def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

N = int(input())
res = N*N*3
for x in range(1,N+1):
    for y in range(1,N+1):
        d = gcd(x,y)
        res += min(y*d//x,(N-x)*d//y)*2
print(res)
