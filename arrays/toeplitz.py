
import math
def toeplitz(matrix):
  row = matrix[0]
  start_coords = []
  end = int(math.ceil(len(row) / 2))  # 5 / 2 -> 3
  for i in range(end):
    start_coords.append((0, i))
  # [(0,0),(0,1),(0,2)]

  for x, y in start_coords:
    value = matrix[x][y]
    while x < len(matrix[0]) and y < len(matrix):
      if matrix[x][y] != value:
        return False
      x += 1
      y += 1
  return True


print(toeplitz([[1, 2, 3, 4], [5, 4, 2, 3], [4, 0, 1, 2]]))
print(toeplitz([[1, 2, 3, 4], [5, 1, 2, 3], [4, 0, 1, 2]]))


# def checkToeplitz(arr):
#   for r in range(len(arr)):
#     for c in range(len(arr[0])):
#       if 0 < r <= len(arr) and 0 < c <= len(arr[0]) and arr[r][c] != arr[r-1][c-1 ]:
#         return False
#   return True
#
# print(checkToeplitz([[1,2,3,4],[5,1,2,3],[6,5,1,2]]))