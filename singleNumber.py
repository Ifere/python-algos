

def isSingle(arr):
    return (2 * sum(set(arr))) - sum(arr)

def isSingle2(arr):
    a = 0
    for num in arr:
        a ^= num
    return a

def singleNumber(self, nums: List[int]) -> int:
    one, two, three, four = 0, 0, 0, 0
    for x in nums:
        three = two & x
        two = (two | (one & x)) & ~three
        one = (one ^ x) & ~three
    return one


print(isSingle2([1,1,2,2,3s]))