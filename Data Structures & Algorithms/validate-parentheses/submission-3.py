class Solution:
    def isValid(self, s: str) -> bool:
        matches = {'(': ')', '{':'}', '[':']'}
        stack = []
        for i in s:
            if i in matches.keys():
                stack.append(i)
            elif i in matches.values():
                if len(stack) > 0:
                    if matches[stack[-1]] == i:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False