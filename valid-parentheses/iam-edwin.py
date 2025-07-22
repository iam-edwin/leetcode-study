class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for bracket in s:
            if bracket in ["(", "{", "["]:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False

                element = stack.pop()
                if bracket == ")" and element != "(":
                    return False
                elif bracket == "}" and element != "{":
                    return False
                elif bracket == "]" and element != "[":
                    return False

        return len(stack) == 0
