class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        count = Counter()
        max_len = 0

        for right in range(len(s)):
            count[s[right]] += 1

            while count[s[right]]>1:
                count[s[left]] -= 1
                left += 1

            max_len = max(max_len , right-left+1)
        return max_len
