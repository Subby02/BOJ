# https://www.acmicpc.net/problem/1002

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())

  dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

  if dist == 0:

    if r1 == r2:
      print(-1)
    else:
      print(0)

  else:
    if r1 < r2:
      r2, r1 = r1, r2

    if r1 + r2 < dist or r1 - r2 > dist:
      print(0)
    elif r1 + r2 > dist > r1 - r2:
      print(2)
    elif r1 + r2 == dist or r1 - r2 == dist:
      print(1)