class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        L, R = 0 , len(newStr)-1

        while L < R:
            if newStr[L] != newStr[R]:
                return False
            else:
                L += 1
                R -= 1
        return True
            
        