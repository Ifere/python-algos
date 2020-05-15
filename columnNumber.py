def columnNumber(string):
    n = len(string)

    def positionof(alphabet):
        return ord(alphabet) - 64
m
    number = 0

    for i in range(len(string)):
        number += 26 ** (n - i - 1) * positionof(string[i])

    return number

print(columnNumber("BCB"))