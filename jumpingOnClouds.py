def jumpingOnClouds(c):
    last = len(c) - 1
    # last is the index of the last number in the list
    jumps = i = 0

    # set the iterable to 0

    # while the iterator is less than the length  of the array

    while i < (last - 2):
        # i += 2 if c[i+2]== 0 else

        i += 2 if c[i + 2] == 0 else 1
        jumps += 1
    # add an extra jump for victory
    return jumps + 1
