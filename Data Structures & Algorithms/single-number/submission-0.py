class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k = 0
        for ch in nums:
            k = k ^ ch
        return k
        