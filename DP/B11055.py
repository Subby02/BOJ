# https://www.acmicpc.net/problem/11055

import sys

input = sys.stdin.readline

n = int(input())

arr = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
  for j in range(i):
    if arr[i] > arr[j]:
      dp[i] = max(dp[j] + arr[i], dp[i])

print(max(dp))
