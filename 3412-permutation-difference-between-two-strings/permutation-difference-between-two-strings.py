class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        pos={}
        for i , ch in enumerate(s):
            pos[ch] = i
        total = 0
        for i, ch in enumerate(t):
            total += abs(pos[ch]-i)
        return total


        