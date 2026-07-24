class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        ans = []

        for num in nums:
            d[num] = d.get(num, 0) + 1
        res = [[k, v] for k, v in d.items()]
        res.sort(key=lambda x: x[1], reverse=True)
        for i in range(k):
            ans.append(res[i][0])
        return ans
        