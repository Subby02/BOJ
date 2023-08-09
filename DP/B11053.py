# https://www.acmicpc.net/problem/11053

import sys

input = sys.stdin.readline

n = int(input())

array = list(map(int,input().split()))

dp = [0] * (n+1)

array.insert(0,0)

for i in range(1,n+1):
  for j in range(i):
    if array[i] > array[j]:
      dp[i] = max(dp[j]+1,dp[i])

print(max(dp))