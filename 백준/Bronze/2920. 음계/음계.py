arr = list(map(int, input().split()))


def solution(numbers):
    first = numbers[0]
    result = "mixed"
    for i, v in enumerate(numbers):
        # 마지막 요소는 검사 안함
        if i < len(numbers) - 1:
            if first == 1:
                # 오름차순 조건
                if v < numbers[i + 1]:
                    result = "ascending"
                else:
                    result = "mixed"
                    break
            elif first == 8:
                # 내림차순 조건
                if v > numbers[i + 1]:
                    result = "descending"
                else:
                    result = "mixed"
                    break
    print(result)


solution(arr)