# https://www.acmicpc.net/problem/2407

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
  dp[i][1] = i
  dp[i][i] = 1

for i in range(2, n):
  for j in range(1, i):
    dp[i + 1][j + 1] = dp[i][j] + dp[i][j + 1]

print(dp[n][m])
