class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        num=0
        j=0
        ans=0
        for i in range(len(nums)):
            while(num&nums[i])!=0:
                num^=nums[j]
                j+=1
            num|=nums[i]
            ans=max(ans,i-j+1)
        return ans
        