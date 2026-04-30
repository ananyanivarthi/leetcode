class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        n = len(nums)
        answer = []
        for i in range(n):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                answer.append(abs(nums[i]))
            else:
                nums[idx] = -nums[idx]
        return answer
        