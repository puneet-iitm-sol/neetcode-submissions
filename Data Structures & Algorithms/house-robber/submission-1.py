class Solution:
    def solve(self,nums,i,dp):
        if i == 0:
            return nums[i]
        if i<0 :
            return 0
        if dp[i]!= -1:
            return dp[i]
        pick = nums[i]+self.solve(nums,i-2,dp)
        not_pick  = 0+self.solve(nums,i-1,dp)
        dp[i]=  max(pick,not_pick)
        return dp[i]
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*len(nums)
        return self.solve(nums,len(nums)-1,dp)
        