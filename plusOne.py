# '''
# Given a non-empty array of digits representing a non-negative integer, increment one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.
#
# Example 1:
#
# Input: [1,2,3]
# Output: [1,2,4]
#
# Explanation: The array represents the integer 123.
# Example 2:
#
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
#
#
# Explanation: The array represents the integer 4321
#
#
#
#
# * [1,2,3] -> [1,2,4]
#
#
# * [1,9] -> [2,0]
#
#            1
# * [2,9,9,9,9,9]
#
# * [9,9,9]
#
# J = 2
# sum = (nums[J] + 1) % 10 # 0
# carry = (nums[J] + 1) // 10 # 1
#
# J = 1
# sum = (nums[J] + 1) % 10 # 0
# carry = (nums[J] + 1) // 10 # 1
#
# J = 0
# sum = (nums[J] + 1) % 10 # 0
# carry = (nums[J] + 1) // 10 # 1
#
# J = -1
# if carry:
#     add carry to the front.
#
# [1,2,3]
#
# J = 2
# sum = 3 + 1 =4 % 10 4
# carry = 4 // 10 = 0
#
#
#
#
#
# * start from end of arr
# * basically keep adding one till we get a sum <= 9
# * sum = nums[J] + 1 % 10 (9+5 = 14, 14 % 10 = 4, 14 // 10 = 1)
# * if I am never able to get a sum <= 9,append 1 to the start of the array.
# * O(n) time, O(1) space
#
#
# [1,2,3]
#
#
# '''
#
# '''
#
# [7,1,9]
#
# [9,9]
#
# '''
#
#
# def add_one(nums):  # [9,9]
#     J = len(nums) - 1  # J = 1
#     carry = 1
#
#     # nums = [0,0]
#     while J >= 0:  # -1 >= 0
#         sum_ = (nums[J] + carry) % 10  # 9+1 % 10 = 0
#         carry = (nums[J] + carry) // 10  # 9+1 // 10 = 1
#         nums[J] = sum_  # nums[0] = 0
#         if carry == 0:  # 1 != 0
#             break
#         J -= 1
#
#     if carry:  # carry  = 0 -> false
#         # inserts carry @ idx 0
#         nums.insert(0, carry)  # [1,0,0]
#
#     return nums
#
#
# print(add_one([1, 2, 3]))
# print(add_one([2, 9]))
# print(add_one([0]))
# print(add_one([9, 9, 9, 9]))
# print(add_one([9]))

isPossible = False
def canReach(x1, y1, x2, y2):
    global isPossible
    # Write your code here
    helper(x1, y1, x2, y2)
    if isPossible:
        return 'YES'
    return 'NO'


def helper(x1, y1, x2, y2, _map = {}):
    global isPossible
    if (x1, y1, x2, y2) in _map:
        print('here')
        if not _map[(x1, y1, x2, y2)]:
            return
    if x1 > x2 or y1 > y2:
        _map[(x1, y1, x2, y2)] = None
        return
    if x1 == x2 and y1 == y2:
        print('yaay')
        isPossible = True
        return
    helper(x1, y1 + x1, x2, y2)
    helper(x1 + y1, y1, x2, y2)
    return

print(canReach(1, 1, 1000, 1000))