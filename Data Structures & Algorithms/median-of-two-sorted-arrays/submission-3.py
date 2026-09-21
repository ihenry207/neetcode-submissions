class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #first we need to merge these tow list
        nums = nums1 + nums2
        nums.sort() 
        
        totalLen = len(nums)
        #first we need to check if there is a real middle if we have odd numbers. then thats the median
        #if odd, return the middle num
        if (len(nums) % 2 == 1):
            return nums[totalLen // 2]
        #else we have even values
        else:
            return (nums[totalLen // 2-1] + nums[totalLen // 2])/ 2.0