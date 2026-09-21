class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            currSum = numbers[left] + numbers[right]

            if currSum == target:
                return [left + 1, right + 1]
            elif currSum < target:
                left += 1
            else:
                right -= 1
        return []
                
        #brute force solution
        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         if (numbers[i] + numbers[j]) == target:
        #             return[i+1, j+1]
        # return []

        # i = 0
        # while i < len(numbers):
        #     j = i+ 1
        #     while j < len(numbers) - 1:
        #         if (numbers[i] + numbers[j]) == target:
        #             return[numbers[i], numbers[j]]
        #         j += 1
        #     i += 1
        # return []