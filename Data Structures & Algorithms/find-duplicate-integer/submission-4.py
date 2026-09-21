class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #we could solve this using a hashset but space is O(n)
        # nums2 = set()
        # for i in range(len(nums)):
        #     if nums[i] in nums2:
        #         return nums[i]
        #     else:
        #         nums2.add(nums[i])
        # return None

        #but since the question did specify to use a O(1), fast and slow pointers
        slow, fast = 0, 0 #acts as the head for a linkedlist

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] #faster node

            if slow == fast:
                break
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
            