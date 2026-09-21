class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        L, R= 0, len(height)-1

        if not height: return 0 #if we have an empty array.
        leftMax, rightMax = height[L], height[R]

        while L < R:
            if leftMax < rightMax:
                L += 1
                leftMax = max(leftMax, height[L])
                res += leftMax - height[L]
            else:
                R -= 1
                rightMax = max(rightMax, height[R])
                res += rightMax -height[R]
        return res