class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum = 0
        for ch in s:
            sum = sum-ord(ch)
        for cha in t:
            sum = sum+ord(cha)
        return chr(sum)
        

        