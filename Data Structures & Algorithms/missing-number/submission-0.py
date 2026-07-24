class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumi = sum(nums)
        n = len(nums)
        taget = ((n)*(n+1))//2
        return taget-sumi

        