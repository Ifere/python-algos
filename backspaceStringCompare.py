# def backspaceCompare(S: str, T: str) -> bool:
#     S = list(S)
#     T = list(T)
#     s = []
#     t = []
#     de = False
#     dt = False
#
#     for i in range(len(S)):
#         if S[i] != "#":
#             de = True
#         if de:
#             if S[i] != "#":
#                 s.append(S[i])
#             if S[i] == "#":
#                 s.pop()
#
#
#     for i in range(len(T)):
#         if T[i] != "#":
#             dt = True
#         if dt:
#             if T[i] != "#":
#                 t.append((T[i]))
#             if T[i] == "#":
#                 t.pop()
#
#
#     return s == t
#
# print(backspaceCompare("ab#c","ad#c"))
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    if len(s) < 2:
        return s == t

    count1 = [0] * 256
    count2 = [0] * 256
    for i in range(len(s)):
        count1[ord(s[i])] += 1
    for i in range(len(t)):
        count2[ord(t[i])] += 1

    for j in list(range(256)):
        print(j)
        if count1[j] != count2[j]:
            print("proverb")
            return False
        return True

print(isAnagram("aa","bb"))



