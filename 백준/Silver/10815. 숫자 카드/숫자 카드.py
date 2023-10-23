import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


N = int(input())  # a의 숫자카드 개수
a = sorted(map(int, input().split()))  # a 카드덱
M = int(input())  # b의 숫자카드 개수
b = list(map(int, input().split()))  # b 카드덱

answer = []

for card in b:
    left = bisect_left(a, card)
    right = bisect_right(a, card)
    answer.append(1 if right - left > 0 else 0)


print(*answer)
