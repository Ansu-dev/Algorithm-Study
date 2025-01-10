import sys

# 입력의 첫 줄에서 N을 읽어옵니다.
n = int(sys.stdin.readline())

# N개의 회의 정보를 저장할 리스트를 초기화합니다.
meetings = []

# N개의 회의 정보를 읽어옵니다.
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    meetings.append((start, end)) # 튜플을 사용하여 메모리 최적화

# 회의를 끝나는 시간 기준으로 정렬합니다.
# 끝나는 시간이 같은 경우, 시작 시간이 빠른 순서대로 정렬합니다.
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0 # 회의실 사용이 가능한 최대 수
last_end_time = -1 # 마지막으로 끝난 회의의 끝나는 시간 (0시가 있기때문에 -1으로 저장)

for meeting in meetings:
    start, end = meeting

    # 마지막으로 회의가끝난 시간보다 시작시간이 더 크면 회의가능
    if start >= last_end_time:
        count += 1 # 사용가능한 회의실로 기억
        last_end_time = end # 끝나는 시간을 기록

print(count)