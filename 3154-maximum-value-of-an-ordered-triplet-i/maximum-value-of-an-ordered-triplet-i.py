class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxx=0
        for i in range(0,len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    maxx=max(maxx,(nums[i]-nums[j])*nums[k])
        return maxx

                    

        