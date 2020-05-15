#     def recurse(current_row, current_col, tr, tc, length, visited):
#     # base case
#     # length to keep track of shortest path
#     #visited is a log of all the positions that we've been in the past
#
#     #base case is when current row = tr and current column = tc
#
#         if current_row == tr and current_col == tc:
#             return length
#
#     # append current position to visited
#         visited.add((current_row, current_col))
#
#     # try all 4 directions, up ,down ,left ,right
#         directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
#         next_moves = []
#     # try out each direction
#         for x, y in directions:
#             new_row = current_row + x
#             new_col = current_col + y
#         # check range valid
#             if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
#             # go to next state
#                 if (new_row, new_col) not in visited:
#                     next_moves.append((new_row, new_col))
#
#     # if no solution
#         if len(next_moves) == 0:
#             return -1
#
#     # otherwise
#         result = float('inf')
#         for move in next_moves:
#             result = min(result, recurse(move[0], move[1], tr, tc, length + 1, set(visited)))
#
#     # if not possible
#         if result == float('inf'):
#             return -1
#         else:
#             return result
#
#     # driver code
#
#
#     visited = set()
#     return recurse(sr, sc, tr, tc, 0, visited)
# import sys
# sys.setrecursionlimit(10**20)
#
# def arrayprint(array):
#     if len(array) == 1:
#         print(array[0])
#         return None
#     else:
#         print(array[0])
#         return arrayprint(array[(len(array)-(len(array) - 1)):])
#
#
# arrayprint([])
#
# def max(arr):
#
#     if array
#
#     else:
#         return max(arr[i], arr[i+1])
# def recur(arr, num = -10000, i= 0):
#     if i < len(arr):
#         if num < arr[i]:
#             num = arr[i]
#         i+=1
#         return recur(arr,num,i)
#     else:
#         return num
#
# print(recur([1,2,5,4,7]))


from flask import Flask, jsonify, make_response, request

app = Flask(__name__)


# Native function

def palindromecheck(str):
    """

        palindromecheck is a fullproof palindrome detector

        detects single word palindromes such as eve or

        multiple word palindromes such as 'nurses run'\



        args: <class 'string'>

        returns: <class 'bool'>



        PS: this function is used in the server handler below to perdorm the

        check on received input from external applications

    """

    list1 = str.split(' ')

    if len(list1) == 1:

        word = str[::-1]

        if word == str:

            return True

        else:

            return False

        pass

    else:

        placehold = []

        placehold1 = []

        for i in range(1, len(list1) + 1):
            placehold.append(list1[-i])

        for i in placehold:
            placehold1.append(i[::-1])

        word = ''.join(i for i in placehold1)

        if word == ''.join(i for i in list1):

            return True

        else:

            return False


# Server Handler

@app.route('/drome', methods=['GET'])
def dromer():
    # data = request.get_json()

    words = request.get_json()['words']

    dict_ = []

    for word in words:

        if palindromecheck(word):
            dict_.append(word)

    return make_response(jsonify({"words": dict_}), 200)


if __name__ == '__main__':
    app.run(debug=True)