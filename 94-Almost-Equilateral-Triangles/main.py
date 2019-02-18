def bs(arr, l, r, x):
    """Binary Search arr from index l to r for x"""
    while l <= r:
        mid = l + (r - l)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return r


# Set up initial state
MAX = 10**18
P = [0]
# Fundamental solution
sol = [2, 1]
i = 1

while P[-1] <= MAX:
    i += 1
    # Implement eq. (5)
    sol = [2*sol[0] + 3*sol[1], sol[0] + 2*sol[1]]
    # Implement eq. (6)
    perim = 2*(sol[0] + (-1)**(i % 2))
    P.append(perim)
del P[0]

prefix = [0]
count = 0
for p in P:
    count += p
    prefix.append(count)

T = int(input())
for _ in range(T):
    N = int(input())
    ans = prefix[bs(P, 0, len(P)-1, N)+1]
    print(ans)
