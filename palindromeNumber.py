# Palindrome Number [Easy]
# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        l = len(x) - 1
        for i in range(len(x)):
            if x[i] != x[l]:
                return False
            l -= 1
        return True
