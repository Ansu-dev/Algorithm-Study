import sys
input =  sys.stdin.readline

N, M = map(int, input().split())


def binary_search(lecture_lengths, target):
    min_size = max(lecture_lengths) # 강의에서 블루레이가 가장 큰값이 최소
    max_size = sum(lecture_lengths) # 모든 강의의 블루레이 합

    result = min_size # 초깃값에 최소 사이즈를 넣음

    while min_size <= max_size:
        mid_size = (min_size + max_size) // 2
        count = 1 # 필요한 블루레이 개수 (최소 1개)
        total = 0 # 현재 블루레이에 녹화된 강의 총 길이

        for length in lecture_lengths:
            if (total + length) > mid_size:
                # 현재 블루레이에선 녹화 할 수 없으니 다른 블루레이로 이동
                count += 1
                total = length # 새로운 블루레이에서 시작
            else:
                # 현재 블루레이에 녹화 추가
                total += length

        if count <= target:
            # 현재 mid_size 값이 가능하므로, 더 작은 값을 시도
            result = mid_size
            max_size = mid_size - 1
        else:
            # 현재 mid_size 값이 불 가능하므로, 더 큰 값을 시도
            min_size = mid_size + 1

    return result


def main():
    lecture_lengths = list(map(int, input().split()))

    result = binary_search(lecture_lengths, M)
    print(result)

main()