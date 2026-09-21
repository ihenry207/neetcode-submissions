class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #for this we use a 2 sum + normal loop to find the number
        res =[]
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l, r = i+1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res

        #Brute force
        # Outputs = set() #pairs
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if(nums[i] + nums[j] + nums[k]) == 0:
        #                 tmp = [nums[i], nums[j], nums[k]]
        #                 Outputs.add(tuple(tmp))
        # return [list(i) for i in Outputs]