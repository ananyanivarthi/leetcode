class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def checknonzero(a:int):
            return "0" not in str(a)
        
        for a in range(1,n):
            b = n-a
            if checknonzero(a) and checknonzero(b):
                return [a,b]


        