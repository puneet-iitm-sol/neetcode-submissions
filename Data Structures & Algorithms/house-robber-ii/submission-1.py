class Solution:
    def solve(self, i, nums, dp):
        if i == 0:
            return nums[0]
        if i < 0:
            return 0

        if dp[i] != -1:
            return dp[i]

        pick = nums[i] + self.solve(i - 2, nums, dp)
        not_pick = self.solve(i - 1, nums, dp)

        dp[i] = max(pick, not_pick)
        return dp[i]

    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        num1 = nums[1:]      # Exclude first house
        num2 = nums[:-1]     # Exclude last house

        dp1 = [-1] * len(num1)
        dp2 = [-1] * len(num2)

        m = self.solve(len(num1) - 1, num1, dp1)
        n = self.solve(len(num2) - 1, num2, dp2)

        return max(m, n)