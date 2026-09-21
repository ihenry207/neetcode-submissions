class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #Pair (start_index, height)+

        for i, h in enumerate(heights):
            start = i
            #while the current bar is shorter than the one on top of the stack
            while stack and stack[-1][1] > h:
                #we stack pop the top of the stack
                index, height = stack.pop()

                #we then calculate the are
                maxArea = max(maxArea, height * (i-index))
                
                # 2. Key trick: Since 'height' was taller than 'h',
                # our new shorter bar 'h' can extend backwards to where 'index' was!
                start = index

            stack.append((start, h))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea

