from math import sqrt

def match(n,digits):
    n *= n
    i = 0
    while n > 0:
        curr = n % 10
        if curr != digits[i]:
            return False
        n //= 100
        i += 1
    return True

ROOTS = {0:(0,0),1:(1,9),4:(2,8),9:(3,7),6:(4,6),5:(5,5)}
N = int(input())
DIGITS = list(map(int,input().split()))
MAX = 0
MIN = 0
for i in range(N):
    new = DIGITS[i]*10**(2*(N-1-i))
    MAX += new + int(9*10**(2*(N-1-i)-1))
    MIN += new
DIGITS.reverse()
MIN = int(sqrt(MIN))
root = ROOTS[DIGITS[0]]
MIN += min((root[0] - (MIN % 10)) % 10,
           (root[1] - (MIN % 10)) % 10)
MAX = int(sqrt(MAX))

n = MIN
while True:
    if match(n,DIGITS):
        print(n)
        break
    increment = root[1] - root[0]
    if increment == 0:
        n += 10 - root[0]
    elif n % 10 == root[0]:
        n += increment
    else:
        n += 10 - increment
