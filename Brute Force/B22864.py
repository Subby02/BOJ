# https://www.acmicpc.net/problem/22864

import sys

input = sys.stdin.readline

a,b,c,m = map(int,input().split())

tire = 0
work = 0

for hour in range(24):
  if tire + a <= m:
    tire += a
    work += b
  else:
    tire -= c
    if tire < 0:
      tire = 0

print(work)