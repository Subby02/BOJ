# https://www.acmicpc.net/problem/9012

import sys

input = sys.stdin.readline

n = int(input())

cnt = 0

for _ in range(n):
  s = input().rstrip()

  cnt = 0
  isNo = False
  for c in s:
    if c == '(':
      cnt += 1
    else:
      cnt -= 1
      if cnt < 0:
        isNo = True
        break

  if cnt != 0:
    isNo = True

  if isNo:
    print('NO')
  else:
    print('YES')