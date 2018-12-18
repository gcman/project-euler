def primes(n):
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes

P = primes(100)
curr = [1,[0]*len(P)]
MAX = int(input())

while True:
    size = curr[0]
    exp = curr[1]
    factors = 1
    for e in exp:
        factors *= 2*e + 1
    factors += 1
    factors //= 2
    if factors >= MAX:
        print(size)
        break
    todo = [[size*P[j], [x+(i==j) for i,x in enumerate(exp)]] for j in range(len(exp))]
    todo.sort(key=lambda x: x[0])
    curr = [todo[0][0],todo[0][1]]
