class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        L= 0
        res = 0

        for R in range(len(s)):
            #Add current character frequency
            count[s[R]] = 1 + count.get(s[R], 0)

            # if replacements needs more than k, then we move left pointer and shrink the window from left
            while (R-L+1) - max(count.values()) > k:
                count[s[L]] -= 1
                L += 1
            #update maximum valid length found so far
            res = max( res, R-L+1)

        return res