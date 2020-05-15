# import collections
# # def sorter(wrd):
# #     wrd = list(wrd);
# #     wrd.sort()
# #     return "".join(wrd)
# #
# #
# # def groupAnagrams(words):
# #     d = {}
# #     a = []
# #     for i in range(len(words)):
# #         wrd = sorter(words[i])
# #         if wrd not in d:
# #             d[wrd] = []
# #
# #     for word in words:
# #         wrd = sorter(word)
# #         if wrd in d:
# #             d[wrd] += [word]
# #
# #     for v in d.values():
# #         a.append(v)
# #     print(a)
# #     return a
# #
# # def groupAnagram(strs):
# #     ans = collections.defaultdict(list)
# #     for s in strs :
# #         count = [0] * 26
# #         for c in s:
# #             count[ord(c) - ord('a')] += 1
# #             ans[tuple(count)].append(s)
# #     return ans.values()
# #
# #
# # # groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# #
# # print(groupAnagram((["eat", "tea", "tan", "ate", "nat", "bat"])))

def sq(num):
    while num > 0:
        num += (num%2)**2
    return num

print(sq(19))