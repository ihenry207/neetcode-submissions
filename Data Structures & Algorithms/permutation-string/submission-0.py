class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is larger than s2, it's impossible to be a substring
        if len(s1) > len(s2): 
            return False
            
        # Target counts
        count1 = Counter(s1)
        # Window counts (just the first len(s1) characters)
        window_count = Counter(s2[:len(s1)])
        
        if count1 == window_count:
            return True
            
        # Slide the window one character at a time
        for i in range(len(s1), len(s2)):
            # 1. Add the new character on the right side of the window
            right_char = s2[i]
            window_count[right_char] += 1

            #remove the left pointer
            left_char = s2[i-len(s1)]
            window_count[left_char] -= 1

            #remove the zero non needed
            if window_count[left_char] == 0:
                del window_count[left_char]
            
            if count1 == window_count:
                return True
        return False