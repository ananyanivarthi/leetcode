from collections import Counter
class Solution:
    @staticmethod
    def isanagram(a,b):
        return Counter(a) == Counter(b)
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack=[]
        for word in words:
            if stack and self.isanagram(stack[-1],word):
                continue
            stack.append(word)
        return stack
        

        