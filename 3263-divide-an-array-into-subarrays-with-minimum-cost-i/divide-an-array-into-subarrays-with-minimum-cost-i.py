class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        min_cost = float('inf')
        right_min = nums[-1]
        for i in range(n-2, 0, -1):
            min_cost = min(min_cost, nums[0] + nums[i] + right_min)
            right_min = min(right_min, nums[i])
        return min_cost
        