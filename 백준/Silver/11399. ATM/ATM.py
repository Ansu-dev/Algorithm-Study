import sys

input = sys.stdin.readline

N = int(input())

times = list(map(int, input().split()))

# 시간이 제일 적게 걸리는 사람 순으로 정렬
times.sort()

use_time = 0
total_use = 0

# 소용된 시간을 합산
for time in times:
    # 앞에 소모한 시간 + 내가 걸리는 시간
    use_time = use_time + time
    # 각 총 걸리는 시간의 합 누적
    total_use += use_time

print(total_use)