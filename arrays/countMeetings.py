# def countMeetings(arrival, departure):
#     a = []
#     invest = len(arrival)
#     d = {}
#
#     ranje = range(min(arrival), max(departure) + 1)
#
#     for i in range(len(arrival)):
#         a += list(range(arrival[i], departure[i] + 1))
#     a.sort()
#     b = list(set(a))
#
#     for i in range(len(a)):
#         if a[i] not in d:
#             d[a[i]] = 1
#         else:
#             d[a[i]] += 1
#
#     print(d)
#     s = 0
#     for k, v in d.items():
#         if v > 1:
#             s += 1
#             invest = 1
#             b.remove(k)
#         if k in b:
#             s += 1
#             b.remove(k)
#     return s
#
#
# print(countMeetings([1, 10, 11], [11, 10, 11]))