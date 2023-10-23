# 가능한 최대의 총 예산
# 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정
# 예산이 오버되면 안됨


# 예산액 총합이 예산요청의 합보다 크면 제일 큰애를 상한선으로?
# 제일큰 예산요청에서 반을 잡고 하면서 반씩 줄여나간다.
import sys

input = sys.stdin.readline

N = int(input())  # 지방의 수
requests = list(map(int, input().split()))  # 각 지방의 예산 요청
M = int(input())  # 총 예산


low = 0
high = max(requests)
mid = (low + high) // 2

answer = 0


def is_possible(mid):
    # 기준이되는 mid값과 예산요청의 값을 비교하여 더 작은값을 sum으로 더함
    # sum의 값이 총 예산보다 적거나 같을 경우만 return
    return sum(min(request, mid) for request in requests) <= M


while low <= high:
    if is_possible(mid):  # mid의 기준값을 넣어 가능한지 판별
        low = mid + 1  # mid에 + 1하여 low 갱신 mid값은 판별하였기 때문에 mid에서 1을 더한값으로 갱신
        answer = mid
    else:
        # high를 mid로 1을 빼준 값을 갱신
        high = mid - 1

    # mid 갱신
    mid = (low + high) // 2

print(answer)