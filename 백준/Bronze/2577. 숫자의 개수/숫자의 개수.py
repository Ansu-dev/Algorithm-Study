arr = [int(input()) for i in range(3)]


def solution(numbers):
    result = 1
    for i in numbers:
        result *= i

    for i in range(10):
        print(str(result).count(str(i)))


solution(arr)