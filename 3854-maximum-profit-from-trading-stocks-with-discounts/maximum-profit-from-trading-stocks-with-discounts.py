from typing import List

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int],
                  hierarchy: List[List[int]], budget: int) -> int:

        tree = [[] for _ in range(n)]
        for u, v in hierarchy:
            tree[u - 1].append(v - 1)

        NEG = -10**15
        dp = [[[NEG] * (budget + 1) for _ in range(2)] for _ in range(n)]

        self.dfs(0, present, future, tree, dp, budget, NEG)

        # CEO has no parent → parentBought = 0
        return max(dp[0][0])

    def dfs(self, u, present, future, tree, dp, budget, NEG):
        for v in tree[u]:
            self.dfs(v, present, future, tree, dp, budget, NEG)

        for parentBought in range(2):

            # ---------- Option 1: DO NOT buy u ----------
            base = [0] + [NEG] * budget

            for v in tree[u]:
                next_base = [NEG] * (budget + 1)

                # parent u NOT bought → child gets NO discount
                child_dp = dp[v][0]

                for b in range(budget + 1):
                    if base[b] == NEG:
                        continue
                    for k in range(budget - b + 1):
                        if child_dp[k] == NEG:
                            continue
                        next_base[b + k] = max(
                            next_base[b + k],
                            base[b] + child_dp[k]
                        )
                base = next_base

            curr = base[:]

            # ---------- Option 2: BUY u ----------
            price = present[u] // 2 if parentBought else present[u]
            profit = future[u] - price

            if price <= budget:
                base = [0] + [NEG] * budget

                for v in tree[u]:
                    next_base = [NEG] * (budget + 1)

                    # parent u BOUGHT → child MAY get discount
                    child_dp = [
                        max(dp[v][0][k], dp[v][1][k])
                        for k in range(budget + 1)
                    ]

                    for b in range(budget + 1):
                        if base[b] == NEG:
                            continue
                        for k in range(budget - b + 1):
                            if child_dp[k] == NEG:
                                continue
                            next_base[b + k] = max(
                                next_base[b + k],
                                base[b] + child_dp[k]
                            )
                    base = next_base

                for b in range(price, budget + 1):
                    if base[b - price] != NEG:
                        curr[b] = max(curr[b], base[b - price] + profit)

            dp[u][parentBought] = curr
