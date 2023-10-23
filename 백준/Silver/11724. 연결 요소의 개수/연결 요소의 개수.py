# 방향 없는 그래프가 주어질 때  연결 요소 개수 => dfs나 bfs가 수행하는 회수
# 연결되는 간선을 그래프로 그려본다.
# 인접 행렬 또는 인접 리스트
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())  # N : 정점의 개수, M : 간선의 개수
graph = [[0] * N for _ in range(N)]  # N * N 빈 행렬을 만듬
# 주어진 input값을 행렬에 표기 간선이 연결된 노드는 1로 표기(방향성이 없는 양방향 그래프)
for _ in range(M):
    # 배열의 인덱슨느0 부터 시작이지만 시작점이 1이기때문에 입력되는값에 -1을 빼준다.
    a, b = map(lambda x: x - 1, map(int, input().split()))
    graph[a][b] = graph[b][a] = 1

# 1번 노드(행) 검사
visited = [False] * N  # lambda를 해주지않으면 +1을 해줘야함  [0, 1, 2, 3, 4, 5, 6]
count = 0


def dfs(row):
    for column in range(N):
        visited[row] = True  # 기준이 되는 노드는 방문했기에 바로 체크
        if graph[row][column] and not visited[column]:  # 1아 있는 노드이고 방문하지 않는 곳
            visited[column] = True  # 기준노드와 연결되어있는 노드 체크
            dfs(column)  # 기준이 되는 노드에 연결된 노드가 있다면 그 노드부터 다시 dfs를 돌려서 연결된 노드가 있나 확인


for row in range(N):
    if visited[row] == False:  # 기준노드에 대한 dfs를 모두돌고도 방문하지 않았다면 다른 연결 요소
        count += 1  # 연결 요소 개수 체크
        dfs(row)  # 기준이 되는 노드와 연결된 노드를 검사


print(count)
