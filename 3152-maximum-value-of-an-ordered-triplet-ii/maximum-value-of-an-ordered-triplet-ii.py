class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        hi,d,ans=0,0,0
        for x in nums:
            ans=max(ans,d*x)
            d=max(d,hi-x)
            hi=max(hi,x)
        return ans

        