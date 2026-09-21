class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0 #initialize area to zero
        L, R = 0, len(heights) - 1 # declare left and right pointer

        while(L < R):
            width = R - L
            height = min(heights[L], heights[R])
            area = max(area, width * height)
            if (heights[L] < heights[R]): #conditions to increase the points or move their position, if the left height is lowernthan the right, we shift ome pos up and vice versa
                L += 1
            else:
                R -= 1
        return area
