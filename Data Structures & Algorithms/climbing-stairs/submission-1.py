class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        def solve(n,dp):
            if n==0:
                return 1
            if n ==1:
                return 1
            if dp[n] != -1:
                return dp[n]
            dp[n] =  solve(n-1,dp)+solve(n-2,dp)
            return dp[n]
        return solve(n,dp)
        