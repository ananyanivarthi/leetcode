class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = [0]*101
        for num in nums:
            freq[num] +=1

        max_freq= max(freq)
        total = sum(count for count in freq if count == max_freq)
        return total
        