import sys
from collections import deque

input =  sys.stdin.readline

N, K = map(int, input().split())

MAX = 200000


def bfs(N, K):
    visited = [False] * (MAX + 1)
    time = [0] * ( MAX + 1)

    queue = deque()
    queue.append(N) # 처음 노드는 방문을 하니 큐에 담아둠
    visited[N] = True # N의 좌표는 방문했으니 방문 체크

    while queue: # queue가 존재할 때까지 반복
        current = queue.popleft() # queue의 첫번째를 현재로 두고 비교

        # 목표에 도달하면 결과 반환
        if current == K:
            return time[current]

        # 가능한 3가지 연산을 수행
        # 여기서 각 노드를 탐색
        for next_position in (current - 1, current + 1, 2 * current):
            # 유효한 위치인지 확인
            if 0 <= next_position <= MAX and not visited[next_position]:
                queue.append(next_position) #
                visited[next_position] = True # 방문 표시
                time[next_position] = time[current] + 1 # 현재 시간 배열에서 1을 더해준채 그 위치에 시간 저장

print(bfs(N, K))
