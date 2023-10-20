# 답이 반드시 존재
# 9개의 숫자중에 7개를뽑아 키의 합이 100이 되는 난쟁이를 오름차순으로 정렬
# 순서에 상관없이 9개중 7개를 뽑는 모든경우의수에서 100이되는 경우 => 조합

from itertools import combinations

heights = [int(input()) for _ in range(9)]

for combi in combinations(heights, 7):  # 배열에서 몇개를 뽑을껀지
    if sum(combi) == 100:
        for height in sorted(combi):
            print(height)
        break
