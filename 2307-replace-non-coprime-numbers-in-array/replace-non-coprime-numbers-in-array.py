import math
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack=[]
        for num in nums:
            stack.append(num)
            while len(stack)>1:
                a,b=stack[-2],stack[-1]
                gcd = math.gcd(a,b)
                if gcd==1:
                    break
                else:
                    lcm = a *b //gcd
                    stack.pop()
                    stack.pop()
                    stack.append(lcm)
        return stack
