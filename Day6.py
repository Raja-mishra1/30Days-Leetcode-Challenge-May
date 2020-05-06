class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        np = sorted(nums)
        return np[n//2] 