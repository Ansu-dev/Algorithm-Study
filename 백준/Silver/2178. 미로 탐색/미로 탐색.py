# 미로 탐색 = 길 찾기
# 최단거리 = bfs
import sys
from collections import deque

input = sys.stdin.readline
dq = deque()

N, M = map(int, input().split())  # N * M크기의 배열 미로
graph = []

# 입력값으로 미로 만들기
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

# 방향키
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def is_valid_coord(nx, ny):
    return 0 <= nx < N and 0 <= ny < M


def bfs():
    dq.append((0, 0))  # 시작점을 queue에 넣음

    # queue가 빌 때까지 반복하기
    while dq:
        x, y = dq.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            # 기준점으로부터 상하 (행값을 비교) 행은 0보다 작으면 안돼고 N값보다 같거나 크면 안된다.
            nx = x + dx[i]
            # 기준점으로부터 좌우 (열값을 비교) 열은 0보다 작으면 안돼고 M값보다 같거나 크면 안된다.ㄴ
            ny = y + dy[i]

            if is_valid_coord(nx, ny) and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1  # 이미 방문한곳은 1이 아닌 방문 숫자의 횟수를 집어넣음
                dq.append((nx, ny))


bfs()


print(graph[N - 1][M - 1])
