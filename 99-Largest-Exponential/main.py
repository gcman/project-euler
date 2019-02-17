from math import log

# Sort pairs by value of a^b
N = int(input())
pairs = [tuple(map(int, input().split())) for _ in range(N)]
pairs.sort(key=lambda x: x[1]*log(x[0]))

# Get K-th smallest value
K = int(input())
print(*pairs[K-1])
