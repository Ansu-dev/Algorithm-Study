# N종류 동전 K의 합
# A - 1, A는 배수관계 => 그리디 사용가능

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]  # N까지의 범위동안 배열을 돌리기 위함
coins.reverse()  # 큰 금액의 동전을 부터 계산하기위한 내림차순 정렬

answer = 0

for coin in coins:
    answer += K // coin  # 몫의 나누기로 잔액에서 동전을 차례로 나눠지는지 몫을 누적저장
    K %= coin  # 동전의 나머지 계산으로 잔액을 차감

print(answer)
