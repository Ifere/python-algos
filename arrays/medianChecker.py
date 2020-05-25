def medianchecker(arr):
    for i in range(len(arr)):
        a = arr[:i+1]
        a.sort()
        mod = len(a) % 2
        re = len(a) // 2
        if mod == 0:
            print(( a[re] + a[re-1] ) / 2)
        else:
            print( a[re] )


medianchecker([2,1,5,3,4,5,2,4,3,1,7,2,0,5])