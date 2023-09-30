# https://www.acmicpc.net/problem/1966

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n, m = map(int, input().split())

  array = list(map(int, input().split()))

  target = m
  cnt = 1
  while array:
    if target == 0 and array[0] == max(array):
      break

    if array[0] == max(array):
      cnt += 1
      array.pop(0)
    else:
      array.append(array.pop(0))

    if target == 0:
      target = len(array)
    target -= 1

  print(cnt)
