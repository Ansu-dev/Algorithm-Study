# 우선 순위 큐 => 어떤값이 제일 작은지 루트 노드에 배치해줌
# 우선 절대값 비교
# 같은 값이있다면 원래값 비교
import sys
import heapq as hq

input = sys.stdin.readline  # 빠른 입출력
pq = []
for _ in range(int(input())):
    x = int(input())
    if x:  # x가 0아 아니면
        hq.heappush(pq, (abs(x), x))  # 절대값, 원소값을 넣어서 튜플로 만듬
    else:
        # 튜플이 비어있는지 확인
        print(
            hq.heappop(pq)[1] if pq else 0
        )  # pq가 비어있지않으면 절대값과 원소값이 가장 작은 튜플 삭제, 비어있다면 0을 출력
