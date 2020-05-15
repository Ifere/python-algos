def merchant(n, ar):
    if n <= 0:
        return 0
    d = {}
    pairs = 0
    for elem in ar:
        if elem in d:
            d[elem] += 1
        else:
            d[elem] = 1

    for k, v in d.items():
        x = v-1
        if v % 2 == 0:
            pairs += v / 2
        else:
            if x % 2 == 0:
                pairs += x / 2

    return pairs


print(merchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))