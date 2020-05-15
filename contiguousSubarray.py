# def maxSubArraySum(a, size):
#     max_so_far = a[0]
#     curr_max = a[0]
#
#     for i in range(1, size):
#         curr_max = max(a[i], curr_max + a[i])
#         max_so_far = max(max_so_far, curr_max)
#
#     return max_so_far
#
#
#
# def sumArray(arr):
#
#
#     maxsum = 0
#     maxend = 0
#
#     for i in range(len(arr)):
#         maxend += arr[i]
#         if maxend < 0:
#             maxend = 0
#         if maxsum < maxend:
#             maxsum = maxend
#     return maxsum
#
# print(maxint)