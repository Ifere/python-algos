
# def palindroma(string):
#     string = string.replace(" ", "")
#     string = string.lower()
#
#     d = {}
#
#     for i in string:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
#
#     odd = 0
#
#     for v in d.values():
#         if v % 2 != 0 and odd == 0:
#             odd += 1
#         elif v % 2 != 0 and odd > 0:
#             return False
#     return True
#
# print(palindroma("mallam"))