

# recursive factorial function
# def factorial(num):
#     # base case
#     if num == 0 or num == 1:
#         return 1
#     # recursive case
#     return num * factorial(num-1)
#


# recursive reversing function
# def re (s):
#     if len(s) < 2:
#         return s
#     return re(s[1:]) + [s[0]]
#

# recursive power function
# def power(a, b):
#     if b == 1:
#         return a
#     return a * power(a, b-1)

# recursive function to print a;l elements in an array
# def prent(a):
#     if len(a) < 2:
#         print(a[-1])
#         return
#     print(a[0])
#     prent(a[1:])

# def palindrome(str):
#     if len(str) < 2:
#         return True

#     else:
#         str[0] == str[-1] and palindrome(str[1:-1])
#


# def anagram(s):
#     string_list = []
#     for ch in s.lower():
#         string_list.append(ch)
#
#     string_dict = {}
#     for ch in string_list:
#         if ch not in string_dict:
#             string_dict[ch] = 1
#         else:
#             string_dict[ch] = string_dict[ch] + 1
#
#     return string_dict
#
# print(anagram("tabs") == anagram("bars"))
# words [word.lower().sort() for word in words]
#
#
# def check_palin(word):
#     for i in xrange(len(word)/2):
#         if word[i] != word[-1*(i+1)]:
#             return False
#     return True
#
# def all_palindromes(string):
#
#     left,right=0,len(string)
#     j=right
#     results=[]
#
#     while left < right-1:
#         temp = string[left:j] #Time complexity O(k)
#         j-=1
#
#         if check_palin(temp):
#             results.append(temp)
#
#         if j<left+2:
#             left+=1
#             j=right
#
#     return list(set(results))
#
# print(all_palindromes("tacocat"))
#
# def all_palindromes(text):
#     """Return list with all palindrome strings within text.
#
#     The base of this algorithm is to start with a given character,
#     and then see if the surrounding characters are equal. If they
#     are equal then it's a palindrome and is added to results set,
#     extend to check if the next character on either side is equal,
#     adding to set if equal, and breaking out of loop if not.
#
#     This needs to be repeated twice, once for palindromes of
#     odd lengths, and once for palindromes of an even length."""
#
#     results = set()
#     text_length = len(text)
#     for idx, char in enumerate(text):
#
#         # Check for longest odd palindrome(s)
#         start, end = idx - 1, idx + 1
#         while start >= 0 and end < text_length and text[start] == text[end]:
#             results.add(text[start:end+1])
#             start -= 1
#             end += 1
#
#         # Check for longest even palindrome(s)
#         start, end = idx, idx + 1
#         while start >= 0 and end < text_length and text[start] == text[end]:
#             results.add(text[start:end+1])
#             start -= 1
#             end += 1
#
#     return list(results)
#
# print(all_palindromes("tacocat"))
#




# def countSentences(words, sentences):
#     out = []
#     _dict = {}
#     for i in words:
#         a = tuple(checkmatrix(i))
#         if a not in _dict:
#             _dict[a] = 1
#         else:
#             _dict[a] += 1
#
#     for j in sentences:
#         sen = j.split()
#         count = 1
#         for i in sen:
#             a = tuple(checkmatrix(i))
#             if a in _dict:
#                 count *= _dict[a]
#                 print(count)
#         out.append(count)
#     return out
#
#
# def checkmatrix(word):
#     arr = [0 for i in range(128)]
#     for i in word:
#         arr[ord(i)] += 1
#     return arr
#
#
# print(countSentences(['the', 'bats', 'tabs', 'in', 'cat', 'act'], ["act tabs in", 'in the act', 'cat the bats']))


# import datetime
#
#
# def todaysDate():
#     x = datetime.datetime.now()
#
#     print("Today is " + x.strftime("%A"))
#
#     print("Current time is " + x.strftime("%H:%M:%S:%p"))
#
#
# todaysDate()


# def InorderSum(root):
# # lnr
# # add inorder predecessor and successor
#     tree = []
#     def Inorder(root):
#         if root:
#             Inorder(root.left)
#             tree.append(root.val)
#             Inorder(root.right)
#         else:
#             return
#     Inorder(root)
#     print(tree)
#     newtree = []
#     for i in range(len(tree)):
#         if i == 0:
#             newtree.append(tree[i+1])
#         elif i == len(tree) - 1:
#             newtree.append(tree[i-1])
#
#         else:
#             newtree.append(tree[i-1]+tree[i+1])
#
#     return newtree
#
#
#
#
#
# class Node:
#
#     def __init__(self, x):
#         self.left = None
#         self.right = None
#         self.val = x
#
#
# ar = Node(10)
# ar.left = Node(5)
# ar.right = Node(15)
# ar.left.left = Node(3)
# ar.left.right = Node(7)
# ar.right.left = Node(13)
# ar.right.right = Node(18)
# #
#
# print(InorderSum(ar))

# def password(a,b):
#     a = list(a)
#     b = list(b)
#     ref = min(len(a), len(b))
#     arr = []
#     print(ref)
#     for i in range(ref):
#         arr.append(a[i])
#         arr.append(b[i])
#     arr += a[ref:] + b[ref:]
#     return "".join(arr)
#
# print(password("hackerank","mountain"))


# def levelOrder(root):
#     if not root:
#         return []
#     ans, level = [], [root]
#     while level:
#         print(level)
#         ans.append([node.val for node in level])
#         print(ans)
#         temp = []
#         print(temp)
#         for node in level:
#             temp.extend([node.left, node.right])
#             print(temp)
#         level = [leaf for leaf in temp if leaf]
#         print(level)
#     return ans
#
#
# print(levelOrder(ar))

# vals = []
#
#
# def rangeSumBST(root, L: int, R: int) -> int:
#     if not root:
#         return 0
#     else:
#         if L <= root.val <= R:
#             vals.append(root.val)
#         rangeSumBST(root.left, L,R)
#         rangeSumBST(root.right,L,R)
#
#
#
#     return sum(vals)
#
#
#
#
# print(happy(19))




# import re
#
#
#
# def emailcheck(str):
#
#     """
#
#         emailCheck uses regex via python3's re module to verify
#
#         that received argument is indeed an email address.
#
#         -------
#
#         type(argument) == <str_class>
#
#         type(return) == <bool_class>
#
#
#
#         emailcheck can also find an email address from within any
#
#         string text, returns False if it finds none.
#
#     """
#
#
#
#     emailreg = re.compile(r'''
#
#         # username
#
#         ([a-zA-Z0-9_\-+%]+|[a-zA-Z0-9\-_%+]+(.\.))
#
#         # @ symbol
#
#         [@]
#
#         # domain name
#
#         [a-zA-Z0-9.-]+
#
#         # dot_something
#
#         (\.[a-zA-Z]{2,4})
#
#     ''',re.VERBOSE)
#
#     try:
#
#         if emailreg.search(str):
#
#             return True
#
#         else:
#
#             return False
#
#     except AttributeError:
#
#         raise False
#
#
#
# print(emailcheck("the email is asqwealupaul36$gmaqwerr32rwil.cdaeom"))
def shifter (arr, d):
    ix = d % len(arr)
    for i in range(len(arr)):
        temp = arr[i]
        arr[i] = arr[ix + i]
        arr[ix+i] = temp
        return arr


print(shifter([1,2,3,4,5], 2))