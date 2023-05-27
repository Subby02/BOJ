# https://www.acmicpc.net/problem/2231

import sys

n = int(sys.stdin.readline())

isExist = False
for i in range(1, n + 1):
  total = i
  value = i
  while value >= 1:
    total += value % 10
    value //= 10
  if total == n:
    isExist = True
    print(i)
    break

if not isExist:
  print(0)
