#LC question 70. Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        if(n<=2):
            return n
        prev1=1
        prev2=2
        ans=0
        for i in range(3,n+1):
            ans=prev1+prev2
            t=prev2
            prev2=ans
            prev1=t
        return ans