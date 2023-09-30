# https://www.acmicpc.net/problem/4153

import sys

input = sys.stdin.readline

while True:
  a = list(map(int, input().split()))
  if a[0] == 0:
    break

  a.sort()
  if a[-1]**2 == a[-2]**2 + a[-3]**2:
    print('right')
  else:
    print('wrong')