# https://www.acmicpc.net/problem/1758

import sys

input = sys.stdin.readline

n = int(input())

array = []
for _ in range(n):
  array.append(int(input()))

array.sort(reverse=True)

total = 0
for i in range(n):
  if array[i] - i > 0:
    total += array[i] - i

print(total)