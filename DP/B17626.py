# https://www.acmicpc.net/problem/17626

import sys
import math

input = sys.stdin.readline

n = int(input())
dp = [1e9] * (n+1)
dp[1] = 1

squre = [1]
for i in range(2,n+1):
  x = math.sqrt(i)
  if x == int(x):
    dp[i] = 1
    squre.append(i)
  else:
    for v in squre[::-1]:
      dp[i] = min(dp[i-v] + 1 , dp[i])

print(dp[n])