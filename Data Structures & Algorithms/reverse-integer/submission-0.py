class Solution:
    def reverse(self, x: int) -> int:
        sign =  1
        if x<0:
            sign = -1
        ans = 0
        x = abs(x)
        while x>0:
            ans = ans*10 + x%10
            x = x//10
        if ans>2**31 -1 or ans<-2**31:
            return 0
        else:  
            return ans*sign
        
        