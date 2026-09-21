from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        #parse the t, target into hash set for each one we have
        target_count = Counter(t)
        window_counts = {}

        have, need = 0, len(target_count)
        res, res_len = [-1, -1] , float("infinity")

        left = 0

        for right in range(len(s)):
            char = s[right]
            window_counts[char] = 1 + window_counts.get(char, 0) # add the char to window count array. 

            # Increase what we have in that current window
            if char in target_count and window_counts[char] == target_count[char]:
                have += 1
            
            # while have == need we shrink window from the left
            while have == need:
                window_size = right - left + 1

                #if we have a smaller window
                if window_size < res_len:
                    res = [left, right]
                    res_len = window_size
                
                left_char = s[left]
                window_counts[left_char] -= 1 #remove left from the tracker array.

                #if removing the left char caused the window to become invalid, decrement have 
                if left_char in target_count and window_counts[left_char] < target_count[left_char]:
                    have -= 1
                
                # move the left pointer towards the shrinking window
                left += 1
        #return the final substring
        l,r = res

        return s[l:r+1] if res_len != float("infinity") else ""



            



