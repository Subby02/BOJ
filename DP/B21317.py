# https://www.acmicpc.net/problem/21317

import sys

input = sys.stdin.readline

n = int(input())

dp = [[1e9] * (2) for _ in range(n+2)]
small_jump = []
big_jump = []

for _ in range(n-1):
  s,b = map(int,input().split())
  small_jump.append(s)
  big_jump.append(b)

k = int(input())

dp[0][0] = 0
dp[0][1] = 0
for i in range(n-1):
  # 매우 큰 점프를 사용하지 않은 값들을 저장하는 부분
  dp[i+1][0] = min(dp[i][0]+small_jump[i],dp[i+1][0])
  dp[i+2][0] = min(dp[i][0]+big_jump[i],dp[i+2][0])

  # 매우 큰 점프를 사용한 값들을 저장하는 부분
  dp[i+1][1] = min(dp[i][1]+small_jump[i],dp[i+1][1])
  dp[i+2][1] = min(dp[i][1]+big_jump[i],dp[i+2][1])

  # 매우 큰 점프를 사용하지 않은 값들을 사용한 값으로 저장해주는 부분
  dp[i+3][1] = min(dp[i][0]+k,dp[i+3][1])

print(min(dp[n-1]))