class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        elif n%2 != 0 or n==0:
            return False
        # while n%2==0:
        #     n=n/2
        # return n==1
        return self.isPowerOfTwo(n/2)


        
            
            