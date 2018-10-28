CONV = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
def rom2num(S):
    S = S[::-1]
    ans = 0
    prev = 0
    for char in S:
        prev = CONV[char]
        if CONV[char] >= prev:
            ans += prev
        else:
            ans -= prev
    return ans

RULES = [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
def num2rom(n):
    ans = ""
    for x in RULES:
        while n >= x[0]:
            ans += x[1]
            n -= x[0]
    return ans

T = int(input())

for _ in range(T):
    S = input().strip()
    print(num2rom(rom2num(S)))
