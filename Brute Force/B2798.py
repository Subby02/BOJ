# https://www.acmicpc.net/problem/2798

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array = list(map(int, input().split()))

close = 0
for i in range(n):
  for j in range(i + 1, n):
    for k in range(j + 1, n):
      total = array[i] + array[j] + array[k]
      if total <= m and m - total < m - close:
        close = total

print(close)
