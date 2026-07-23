class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        k = set()
        for ch in nums:
            if ch in k:
                return True
            else:
                k.add(ch)
        return False 



        