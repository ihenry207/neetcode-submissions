class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of unresolved opening brackets (LIFO order)
        stack = []

        # Map each closing bracket to its corresponding opening bracket
        closeToOpen = {")": "(", "}": "{", "]": "["}

        for c in s:
        # If the character is a closing bracket (key in our dictionary)
            if c in closeToOpen:
                # Check if the stack has elements and the top matches the required open bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()  # Matched pair found, remove the opening bracket
                else:
                    return False  # Mismatch found, or stack was empty when closing bracket appeared

            # If the character is an opening bracket, push it onto the stack
            else:
                stack.append(c)

        # If the stack is empty, all brackets were properly matched and closed
        return True if not stack else False
        