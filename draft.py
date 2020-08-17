"""
Newton's method

ng = 1/2(og+ n)/og
"""

def root(num, g):
    r = num/2
    for i in range(g):
        r =  1/2 * (r + (num/r))
    return r

print(root(9, 3))