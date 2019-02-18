from math import sqrt, ceil


def triangle(n):
    return n*(n+1)//2


def rectangles(m, n):
    return triangle(m)*triangle(n)


def closest_match(target):
    closest = target
    best_area = 0
    # Starting point
    m = ceil(sqrt(2*target))
    n = 1
    while m >= n:
        count = rectangles(m, n)
        error = abs(target-count)
        area = m*n
        # Closer to target than before
        if error < closest:
            closest = error
            best_area = area
        # Bigger area than before
        elif error == closest:
            best_area = max(area, best_area)
        if count > target:
            m -= 1
        else:
            n += 1
    return best_area


T = int(input())
for _ in range(T):
    N = int(input())
    print(closest_match(N))
