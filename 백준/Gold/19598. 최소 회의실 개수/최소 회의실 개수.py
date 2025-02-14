import sys
import heapq

# 입력 받기
n = int(sys.stdin.readline().strip())
meetings = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 회의 시작 시간을 기준으로 정렬 (같은 경우 종료 시간 기준 정렬)
meetings.sort()

# 우선순위 큐 (최소 힙)
room_heap = []
heapq.heappush(room_heap, meetings[0][1])  # 첫 번째 회의의 종료 시간 추가

# 모든 회의 처리
for i in range(1, n):
    start, end = meetings[i]
    
    # 가장 빨리 끝나는 회의의 종료 시간이 현재 회의 시작 시간보다 작거나 같다면 같은 회의실 사용 가능
    if room_heap[0] <= start:
        heapq.heappop(room_heap)  # 기존 회의실을 사용하므로 제거
    
    # 현재 회의 종료 시간을 힙에 추가 (새로운 회의실 필요할 수도 있음)
    heapq.heappush(room_heap, end)

# 필요한 최소 회의실 개수 출력
print(len(room_heap))