class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        r = l = 0
        q = collections.deque() #the deque will store indexes
        output = [] #output list

        while r < len(nums):
            #we need to first pop the smaller values from the q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            #remove left val from window
            if l > q[0]:
                q.popleft()
            
            if(r+1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        
        return output