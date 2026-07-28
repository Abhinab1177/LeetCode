class Solution:
    def isPalindrome(self, n: int) -> bool:
        if n < 0:
            return False

        temp = n
        rev = 0

        while n > 0:
            r = n % 10
            rev = rev * 10 + r
            n= n//10

        return temp == rev