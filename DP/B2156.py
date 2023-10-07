# https://www.acmicpc.net/problem/2156

import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 2)
array = []
for _ in range(n):
  array.append(int(input()))

array += [0, 0]

dp[0] = array[0]
dp[1] = array[0] + array[1]
dp[2] = max(dp[1], array[0] + array[2], array[1] + array[2])
for i in range(3, n):
  dp[i] = max(dp[i - 1], dp[i - 2] + array[i],
              dp[i - 3] + array[i - 1] + array[i])

print(max(dp))
