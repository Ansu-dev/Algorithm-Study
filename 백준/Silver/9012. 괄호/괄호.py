t = int(input())


for _ in range(t):
    stk = []
    isVps = True
    for ch in input():
        if ch == "(":
            stk.append(ch)
        else:
            # stack size가 1이상일 경우
            if stk:  # 배열의 size가 0이 아닐때
                stk.pop()
            else:
                isVps = False
                break

    if stk:
        isVps = False

    print("YES" if isVps else "NO")


