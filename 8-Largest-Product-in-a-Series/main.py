def substrings(s, k):
    """Find k-length substrings of string s"""
    out = []
    n = len(s)
    for i in range(n-k+1):
        out.append(s[i:i+k])
    return out


def string_prod(s):
    """Find the product of the digits of an integer
    given its string representation s"""
    ans = 1
    for x in s:
        ans *= int(x)
    return ans


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    S = input().strip()
    # Brute force each substring
    ans = max([string_prod(x) for x in substrings(S, K)])
    print(ans)
