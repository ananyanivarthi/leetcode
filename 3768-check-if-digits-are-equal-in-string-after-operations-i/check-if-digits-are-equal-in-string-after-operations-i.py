import math

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        digits = [int(c) for c in s]
        
        left = 0
        right = 0
        
        for i in range(n - 1):
            left = (left + digits[i] * math.comb(n - 2, i)) % 10
            right = (right + digits[i + 1] * math.comb(n - 2, i)) % 10
        
        return left == right
