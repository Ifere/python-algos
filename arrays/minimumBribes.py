def minimumBribes(q):
    bribes = 0
    for i in range(len(q)-1,-1,-1):
        #reverse loop iteration
        if q[i] - (i + 1) > 2:
            #check if the
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2),i):
            if q[j] > q[i]:
                bribes+=1
    print(bribes)
