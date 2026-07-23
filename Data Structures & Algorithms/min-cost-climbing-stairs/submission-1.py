class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp =  [-1]*(n+1)
        def solve(i,dp):
            if i == 0:
                return cost[0]
            if i == 1:
                return cost[1]
            if dp[i] != -1:
                return dp[i] 

            dp[i] =  cost[i] + min(solve(i-1,dp), solve(i-2,dp))
            return dp[i]

        

        return min(solve(n-1,dp), solve(n-2,dp))