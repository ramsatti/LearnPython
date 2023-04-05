def parenthesisCheck(s: str) -> bool:
    stack = []
    closeToOpen = {')': '(', ']': '[', '}': '{'}
           
    for ch in s:
        if ch in closeToOpen:
            if stack and stack[-1] == closeToOpen[ch]:
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)

    return not stack

str = input('Enter String w/ Parenthesis: ')
isGood = parenthesisCheck(str)
print(isGood)