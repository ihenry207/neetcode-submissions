class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums2 = set()
        duplicates = set()
        for i in range(len(nums)):
            if nums[i] in nums2:
                return nums[i]
            else:
                nums2.add(nums[i])
        return None
            