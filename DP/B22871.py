# https://www.acmicpc.net/problem/22871

import sys

input = sys.stdin.readline

n = int(input())

array = list(map(int, input().split()))

dp = [0] + [1e9] * (n-1)

for i in range(1,n):
  for j in range(i):
    power = max((i-j) * (1+abs(array[i]-array[j])),dp[j])
    dp[i] = min(dp[i],power)

print(dp[-1])