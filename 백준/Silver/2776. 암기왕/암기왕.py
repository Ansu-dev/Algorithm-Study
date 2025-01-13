import sys
input =  sys.stdin.readline
# T 테스트 케이스
T = int(input())


# 집합 set을 사용하여 풀이
# O(T * (N + M)) => 이진 탐색보다 효율적
for _ in range(T):
    # N 수첩1에 입력받을 정수의 개수
    N = int(input())
    note_1 = set(map(int, input().split())) # 집합 사용
    # M 수첩2에 입력받을 정수의 개수
    M = int(input())
    # 숫자 순서대로 있어야 하므로
    note_2 = list(map(int, input().split()))

    for num2 in note_2:
        if num2 in note_1:
            print(1)
        else:
            print(0)