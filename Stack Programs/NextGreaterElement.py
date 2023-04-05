def greaterElement(aray):
    la = len(aray)
    stack = []
    result = [-1] * la

    for i in range(la):
        while stack and aray[stack[-1]] < aray[i]:
            remover = stack.pop()
            result[remover] = aray[i]
        stack.append(i)
    return result


arr = [1, 2, 3, 4]
ans = greaterElement(arr)
print(ans)