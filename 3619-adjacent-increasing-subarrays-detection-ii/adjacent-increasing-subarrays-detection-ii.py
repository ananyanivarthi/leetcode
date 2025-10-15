class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return 1
        
        l = 0  # Length of previous increasing sequence
        c = 1  # Length of current increasing sequence
        m = 0  # Maximum k found so far
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                c += 1
            else:
                m = max(m, max(c // 2, min(c, l)))
                l = c
                c = 1
        
        m = max(m, max(c // 2, min(c, l)))
        return m
