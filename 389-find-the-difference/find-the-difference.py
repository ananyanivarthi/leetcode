class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for ch in s:
            result = result ^ ord(ch)
        for cha in t:
            result = result ^ ord(cha)
        return chr(result)
        