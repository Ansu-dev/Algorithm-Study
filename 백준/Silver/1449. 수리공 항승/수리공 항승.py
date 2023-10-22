N, L = map(int, input().split())
locations = sorted(list(map(int, input().split())))  # 물이 새는 위치


start = locations[0] - 0.5
end = start + L
answer = 1

for location in locations:
    if start <= location + 0.5 <= end:  # 물이 새는 위치의 -0.5~+-0.5의 테이프를 붙여야 물이 새지 않는다.
        continue
    else:
        answer += 1
        start = location - 0.5
        end = start + L

print(answer)
