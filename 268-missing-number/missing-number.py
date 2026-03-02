class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        missing = n
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing