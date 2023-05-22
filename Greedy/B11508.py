# https://www.acmicpc.net/problem/11508

import sys

input = sys.stdin.readline

n = int(input())

array = []
for _ in range(n):
  array.append(int(input()))

array.sort(reverse=True)

total = 0
for i in range(n):
  if (i+1) % 3 != 0:
    total += array[i]

print(total)