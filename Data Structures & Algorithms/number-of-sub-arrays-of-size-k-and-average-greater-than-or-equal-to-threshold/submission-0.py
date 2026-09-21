class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        currSum = sum(arr[:k-1]) #find the sum of the first window.

        for L in range(len(arr) - k + 1):# alredy say where we are going to end.
            currSum += arr[L+k-1] # add value at the right pointer.
            if(currSum / k) >= threshold:
                res += 1
            currSum -= arr[L]# substarct the value at the most left

        return res
            
