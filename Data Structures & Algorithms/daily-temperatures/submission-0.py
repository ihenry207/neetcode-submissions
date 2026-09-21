class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) #create already zeros in the list of rturn 
        stack = [] #pair [temp, index]

        for i, t in enumerate(temperatures): #we want to enumerate the index and value
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res