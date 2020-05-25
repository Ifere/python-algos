def repeatedString(s, n):
    sum = len(s)
    m = n % sum
    r = n // sum

    count = 0
    othercount = 0
    for i in s:
        if "a" == i:
            count += 1
    return count * r
    if m != 0:
        slice = s[:m]
        for i in slice:
            if "a" == i:
                othercount += 1
                print(othercount)
    return (count * r) + othercount
