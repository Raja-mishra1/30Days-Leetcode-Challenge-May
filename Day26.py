class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0 : -1}
        res = 0
        s = 0
        for i, num in enumerate(nums):
            s += num - 0.5
            if s in d: 
                res = max(res, i - d[s])
            else: 
                d[s] = i
        return res
