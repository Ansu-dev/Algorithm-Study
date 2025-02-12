import sys
import heapq

def main():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    beers = []
    
    # 각 맥주의 (도수 레벨, 선호도)를 튜플로 저장합니다.
    for _ in range(K):
        v, c = map(int, input().split())
        beers.append((c, v))
    
    # 도수 레벨(c)을 기준으로 오름차순 정렬합니다.
    beers.sort(key=lambda x: x[0])
    
    # min-heap을 사용해 현재까지 선택한 맥주들의 선호도 중, N개 중 가장 작은 선호도들을 관리합니다.
    heap = []
    current_sum = 0  # 현재 heap에 담긴 맥주들의 선호도 합
    answer = -1
    
    # 도수 레벨이 낮은 맥주부터 순차적으로 고려합니다.
    for c, v in beers:
        heapq.heappush(heap, v)
        current_sum += v
        
        # 만약 heap에 담긴 맥주 수가 N개를 초과하면, 선호도가 가장 낮은 맥주 하나를 제거합니다.
        if len(heap) > N:
            current_sum -= heapq.heappop(heap)
        
        # 현재까지 선택한 맥주가 N개이며, 선호도 합이 M 이상이면 현재 도수 레벨 c가 최소 간 레벨이 됩니다.
        if len(heap) == N and current_sum >= M:
            answer = c
            break

    print(answer)

main()