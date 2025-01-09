import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
MAX = 50 + 10

dir_row = [1, -1, 0, 0]
dir_col = [0, 0, 1, -1]

# [1,0]: 아래쪽, [-1, 0]: 위쪽, [0, 1]: 오른쪽, [0, -1]: 왼쪽


def dfs(y, x):
    global visited
    visited[y][x] = True
    for dirIdx in range(4):
        newY = y + dir_row[dirIdx] # 상하로 움직임
        newX = x + dir_col[dirIdx] # 좌우로 움직임
        if graph[newY][newX] and not visited[newY][newX]: # 배추는 있지만 방문한 적이 없다면
            dfs(newY, newX) # 배추있는곳에서 다시 dfs를 실행

# 0. 입력 및 초기화
T = int(input())
for _ in range(T):
    # visited를 활용하여 풀기
    M, N, K = map(int, input().split()) # M 가로 길이, N 세로 길이, K 배추가 심어져 있는 위치의 개수
    graph = [[False] * MAX for _ in range(MAX)]
    visited = [[False] * MAX for _ in range(MAX)]
    # 1. 그래프 정보 입력
    for _ in range(K): # 배추의 개수만큼 반복문
        x, y = map(int, input().split())
        graph[y + 1][x + 1] = True # (1,1) 부터 시작

    # 2. 방문하지 않은 지점부터 dfs 돌기
    answer = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if graph[i][j] and not visited[i][j]:
                dfs(i, j)
                answer += 1
    print(answer)