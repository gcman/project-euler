S = [(i,1) for i in range(1,21)]
S.append((25,1))
D = [(2*i,2) for i in range(1,21)]
D.append((50,2))
T = [(3*i,3) for i in range(1,21)]
ALL = S + D + T

def count(N):
    ans = 0
    for k in ALL:
        ans += len([y for y in sorted(ALL,key=lambda x: x[0]) if y[0] == N - k[0] and y[0] >= k[0]])
    return ans

ANS = 0
for N in range(100):
    for d in D:
        print(N,count(N-d[0]))
        ANS += count(N-d[0])
print(ANS)
