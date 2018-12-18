from math import e

MAX = int(1e6)
memo = [0] * 5
count = 0
for n in range(5,MAX+1):
    d = int(round(n/e))
    while d%2 == 0:
        d //= 2
    while d%5 == 0:
        d //= 5
    if n%d == 0:
        count -= n
    else:
        count += n
    memo.append(count)

T = int(input())
for _ in range(T):
    print(memo[int(input())])
