

def stock(arr):
    d = {}

    for i in range(len(arr)):
        if arr[i] < max(arr[i:]):
            d[arr[i]] = max(arr[i:])
    print(d)



def maxp(prices):
    n= len(prices)
    profit = 0
    for i in range(1,n):
        profit += max(prices[i] - prices[i-1], 0)
    return profit




print(stock([7,1,5,3,6,4,3,4,2]))