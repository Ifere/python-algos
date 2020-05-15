
def next(x):
    sum = 0
    while x != 0:
        sum += (x % 10) ** 2
        x //= 10
    return sum

def happy(n):
    t = n
    h = next(n)
    while (t != h):
        t = next(t)
        h = next(next(h))
    return t ==1