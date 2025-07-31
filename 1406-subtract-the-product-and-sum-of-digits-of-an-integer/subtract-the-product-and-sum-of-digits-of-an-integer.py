class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        prod = 1
        add = 0
        while temp>0:
            r = temp%10
            add = add+r
            prod = prod*r
            temp=temp//10
        res = (prod - add)
        return res
