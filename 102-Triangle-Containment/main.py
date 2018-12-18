def area(a,b,c):
    return abs((a[0]-c[0])*(b[1]-a[1])-(a[0]-b[0])*(c[1]-a[1]))

N = int(input())
count = 0
for _ in range(N):
    P = list(map(int,input().split()))
    A = (P[0],P[1])
    B = (P[2],P[3])
    C = (P[4],P[5])
    O = (0,0)
    if area(A,B,C) == area(A,B,O) + area(B,C,O) + area(A,C,O):
        count += 1
print(count)
