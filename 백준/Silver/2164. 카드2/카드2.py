from collections import deque

N = int(input())
dq = deque(range(1, N + 1))


# 맨앞에 값을 삭제한다.
# 그다음 값을 맨 뒤로 옮긴다.
# 시간복잡도 O(1)
while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())  # 맨앞에서 뺀값을 맨뒤로 넣어준다.

print(dq.pop())
