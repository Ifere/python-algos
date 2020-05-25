import math
def romanArabic(num):
    arr = []
    romans = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XV": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }
    for k,v in romans.items():
        div = math.floor(num/v)
        if div >= 0:
            for i in range(div):
                arr.append(k)
        num %= v
    return "".join(arr)


print(romanArabic(956))
