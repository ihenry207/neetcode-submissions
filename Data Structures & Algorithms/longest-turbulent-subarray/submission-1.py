class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        L = 0
        R = 1
        prev =""

        while R < len(arr):
            if arr[R-1] > arr[R] and prev != ">":
                res = max(res, R-L+1)
                R += 1
                prev = ">"
            elif arr[R-1] < arr[R] and prev != "<":
                res = max(res, R-L+1)
                R += 1
                prev = "<"
            else:
                # we basically want to skip the equals sign
                R = R + 1 if arr[R] == arr[R-1] else R
                # here if there is a turbulent number, we then skip all the way to R -1 right before R. 
                L = R -1
                prev = ""
        return res

