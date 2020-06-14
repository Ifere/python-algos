'''

input = 'babad'
output = 'b' , 'a', 'bab', 'aba'

function for expanding and returning palindrome at current index

function for iterating through the palindromic string
'''

test = 'cababad'


def longest(s):
    largest = ""

    for i in range(len(s)):
        palOdd = expander(s, i, i)
        palEven = expander(s, i, i + 1)

        largest = palOdd if len(palOdd) > len(palEven) else palEven

        largest = largest if len(largest) >= len(largest) else largest

        print(palOdd)
        print(palEven)

        return largest


def expander(st, left, right):
    l = 0
    r = 0
    while left >= 0 and right < len(st):
        if st[left] == st[right]:
            l = left
            r = right
        else:
            break
            left -= 1
            right += 1

    return st[l:r + 1]


def longPal(s):
    import collections
    all_subs = []
    len_track = collections.defaultdict(int)

    def isPal(s):
        return s == s[::-1]

    s = 'babad'

    for start in range(0, len(s)):
        all_subs.append(s[start])
        for rest in range(start + 1, len(s)):
            all_subs.append(s[start: rest + 1])

    max_length = -float('inf')
    for sub in all_subs:
        if isPal(sub):
            len_track[sub] = len(sub)
            max_length = max(max_length, len(sub))

    print(len_track)
    print(len((all_subs)))
    print(all_subs)
    for sub in len_track:
        if len_track[sub] == max_length:
            return sub


def longPalOpt(s):
    max_exp = -float('inf')
    left_bound = 0
    right_bound = 0

    def middleExpansion(s, left, right):
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1

            else:
                break

        return (right - left) - 1

    if s == "" or s == None:
        return 0

    for i in range(0, len(s)):
        even_exp = middleExpansion(s, i, i + 1)
        odd_exp = middleExpansion(s, i, i)
        actual_exp = max(even_exp, odd_exp)

        if actual_exp > max_exp:
            left_bound = i - (actual_exp - 1) // 2
            right_bound = i + (actual_exp // 2)
            max_exp = actual_exp

    return s[left_bound:right_bound + 1]


print(longest(test))















