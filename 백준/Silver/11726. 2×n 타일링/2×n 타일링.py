# 2 x n의 타일
# 방법의 수
# 1 x 2, 2 x 1 타일로 채우는 방법
n = int(input())

MOD = 10007

# bottom up 방식은 최대로 들어올 수 있는 값을 미리 채워넣음
dp = [0] * 1001
dp[1] = 1  # 2 x 1 = 1
dp[2] = 2  # 2 x 2 = 2

# 1 = f(1)
# 2 = f(2)
# 3 = f(3)
# 점화식을 짜는게 제일 중요
# f(n) = f(n - 1) + f(n - 2)


for i in range(3, 1001):
    dp[i] = (dp[i - 1] + dp[i - 2]) % MOD


print(dp[n])
