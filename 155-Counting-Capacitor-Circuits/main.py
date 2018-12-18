def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while a:
        a, b = b % a, a
    return b

MAX = 18
D = [{},{(1,1)}]
all = set()
all.update(D[1])
for i in range(2,MAX + 1):
    curr = set()
    for j in range(1,i//2 + 1):
        for (n0,d0) in D[j]:
            for (n1,d1) in D[i - j]:
                part_sum = n0*d1 + n1*d0
                num_prod = n0*n1
                den_prod = d0*d1
                num_G = gcd(part_sum,num_prod)
                den_G = gcd(part_sum,den_prod)
                curr.add((part_sum//den_G,den_prod//den_G))
                curr.add((num_prod//num_G,part_sum//num_G))
    D.append(curr)
    all.update(curr)
print(len(all))
