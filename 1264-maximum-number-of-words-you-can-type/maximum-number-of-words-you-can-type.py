class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenletters = set(brokenLetters)
        words = text.split(" ")
        count = 0

        for word in words:
            bad = False
            for c in word:
                if c in brokenletters:
                    bad=True
                    break
            if not bad:
                count+=1
        return count
            

        