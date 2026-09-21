class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #We create a key pair array
        #zip is basically used when Coupling Car Data: The speed at speed[i] belongs strictly to the car at position[i]. zip(position, speed) bundles each car's position and speed together into a single tuple (p, s).
        pair = [(p, s) for p, s in zip(position, speed)]

        pair.sort(reverse = True)
        stack =[]

        for p, s in pair: #Reverse order
            # Calculate time needed for current car to reach target
            stack.append((target-p)/s)
            #the the newer item item is less that the front one, that means they collided
            if len(stack) >= 2 and stack[-1] <= stack [-2]: 
                stack.pop()
        return len(stack)
        