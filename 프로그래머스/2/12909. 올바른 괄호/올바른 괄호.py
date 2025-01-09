def solution(s):
    answer = True
    stack = []
    for v in s:
        if v == '(':
            stack.append(v)
        else:
            if len(stack) == 0: # )는 스택에 쌓지 않으니 스택이 비었다면 False
                return False
            else:
                stack.pop()

    print(stack)

    if len(stack) != 0:
        return False
    return True