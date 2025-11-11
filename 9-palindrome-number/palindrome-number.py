class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        y = 0
        while temp>0:
            rem = temp % 10
            y = y*10 + rem
            temp=temp//10
        if y == x:
            return True
        else:
            return False