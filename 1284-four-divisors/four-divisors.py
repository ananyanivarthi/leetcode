class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0

        for n in nums:
            count = 0          # number of non-trivial divisor pairs
            div = 0            # to store the divisor i

            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    # perfect square case → reject
                    if i == n // i:
                        count = 2
                        break

                    count += 1
                    div = i

                    # more than one divisor pair → reject
                    if count > 1:
                        break

            # exactly one divisor pair → 4 divisors
            if count == 1:
                ans += 1 + div + (n // div) + n

        return ans
