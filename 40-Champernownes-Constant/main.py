MAX = 10**18


def loc(dig):
    """Find block that dig is part of
    and its position in the block"""
    # block in which dig resides
    block = 1
    # no. of integers in block-th block
    fact = 9
    # fact * block represents the length of the block-th block
    # If what's left of dig is less than fact*block,
    # then dig is partway through 'block'; we've found the right block
    # Make sure block is not too big, based on input
    while dig - fact*block > 0 and fact*block < 9*MAX:
        # subtract away the length of the currrent block
        dig -= fact*block
        # Move to the next block
        block += 1
        # The next block contains ten times more numbers
        fact *= 10
    # Subtract 1 to zero-index position of dig in block
    return dig-1, block


def digit(n):
    """n-th digit of Champernowne's constant"""
    pos, block = loc(n)
    # First num in block is 10**(block-1)
    # pos//block nums precede the number that the n-th digit is part of
    # So the number dig is part of is 10**(block-1) + pos//block
    # dig is the pos%block-th digit in its number
    dig = int(str(10**(block-1)+pos//block)[pos % block])
    return dig


def dig_prod(arr):
    """Product of i-th digits of Champ. constant,
    where i are the elements of arr"""
    out = 1
    for x in arr:
        out *= digit(x)
    return out


T = int(input())
for _ in range(T):
    D = map(int, input().split())
    print(dig_prod(D))
