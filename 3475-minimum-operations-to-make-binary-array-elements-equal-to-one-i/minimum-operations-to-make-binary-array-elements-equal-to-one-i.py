class Solution:
    def minOperations(self, nums: List[int]) -> int:
        num_op=0
        for i in range(len(nums)):
            if nums[i]==1:
                continue
            if i+2>=len(nums):
                return -1
            num_op+=1
            for j in range(i,i+3):
                nums[j]^=1
        return num_op