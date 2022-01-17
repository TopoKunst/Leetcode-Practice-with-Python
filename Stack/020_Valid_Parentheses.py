class Solution:
    def isValid(self, s: str) -> bool:
        # dictionary
        dict = {')': '(', ']': '[', '}': '{'}
        # stack
        stack = []

        # iteration
        for i in range(len(s)):
            if s[i] in dict.values():
                stack.append(s[i])
            elif s[i] in dict.keys():
                if stack == [] or stack.pop() != dict[s[i]]:
                    return False

        return stack == []