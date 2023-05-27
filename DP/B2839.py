# https://www.acmicpc.net/problem/2839

import sys

input = sys.stdin.readline

n = int(input())
dp = [1e9] * (n+6)

dp[0] = 0

for i in range(n+1):
  dp[i+3] = min(dp[i+3] , dp[i] + 1)
  dp[i+5] = min(dp[i+5] , dp[i] + 1)


if dp[n] == 1e9:
  print(-1)
else:
  print(dp[n])