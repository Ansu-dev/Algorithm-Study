arr = [int(input()) for i in range(9)]


def solution(numbers):
    _max = max(numbers)
    _index = numbers.index(_max) + 1
    print(_max)
    print(_index)


solution(arr)