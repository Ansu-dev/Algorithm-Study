import sys

input = sys.stdin.readline

N, M = map(int, input().split())  # N : 나무 수, M : 가져가려는 나무의 길이
trees = list(map(int, input().split()))  # 나무


low = 0
high = max(trees)
mid = (low + high) // 2

answer = 0  # 절단기의 높이


# 현재 나무의 총합에서 필요한 나무 길이 M이 되려면 절단기의 높이
# 문제에 따라 구하려는 기준의 공식이 바뀜
def is_possible(mid):
    return (
        sum((tree - mid) if tree > mid else 0 for tree in trees) >= M
    )  # 나무의 높이에서 - mid값을 뺀 합들이 7보다 크거나 같을 때


# 파라메트릭 서치에서는 거의 고정값
while low <= high:
    if is_possible(mid):
        low = mid + 1
        answer = mid
    else:
        high = mid - 1
    mid = (low + high) // 2


print(answer)
