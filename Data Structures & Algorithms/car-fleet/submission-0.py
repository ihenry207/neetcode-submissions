class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #We create a key pair array
        pair = [(p, s) for p, s in zip(position, speed)]

        pair.sort(reverse = True)
        stack =[]

        for p, s in pair: #Reverse order
            stack.append((target-p)/s)
            #the the newer item item is less that the front one, that means they collided
            if len(stack) >= 2 and stack[-1] <= stack [-2]: 
                stack.pop()
        return len(stack)
        