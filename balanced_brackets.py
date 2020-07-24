def balancedBrackets(string):
    brackets = {
		"{": "}",
		"(": ")",
		"[": "]"
    }
    stack = []
    for item in string:
        if item in brackets:
            stack.append(item)
        elif item in brackets.values():
            if len(stack) == 0:
                return False
            if brackets[stack[-1]] == item:
                stack.pop()
            else:
                return False
    
    return len(stack) == 0

input_str = "([])(){}(())()()"
print(balancedBrackets(input_str))