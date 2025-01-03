class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum=sum(nums)
        prefix_sum=0
        count=0
        n=len(nums)
        for i in range(n-1):
            prefix_sum+=nums[i]
            right_sum=total_sum-prefix_sum
            if prefix_sum>=right_sum:
                count+=1
        return count