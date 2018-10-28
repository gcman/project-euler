def bs(arr, l, r, x):
    while l <= r:
        mid = l + (r - l)//2;
        if arr[mid] == x:
            return arr[mid-1]
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return arr[r]

def order(a,m):
    for i in range(1,m+1):
        if pow(a,i,m) == 1:
            return i

MAX = 10000
longest = 0
prefix = [3]
for d in range(4,MAX+1):
    if d%2 != 0 and d%5 != 0:
        O = order(10,d)
        if O > longest:
            longest = O
            prefix.append(d)

T = int(input())
for _ in range(T):
    N = int(input())
    print(bs(prefix,0,len(prefix)-1,N))
