class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Initiate a new string to copy the string in
        newStr = ""

        #We only get things that are aplha numeric
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        #we initiate a index to parse through those 2 pointers
        L, R = 0 , len(newStr)-1

        #Iterate through the aarray of this new string
        while L < R:
            if newStr[L] != newStr[R]:
                return False
            else:
                L += 1
                R -= 1
        return True
            
        