# https://www.acmicpc.net/problem/2961

import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())

array = []
for _ in range(n):
  a, b = map(int, input().split())
  array.append((a, b))

min_value = 1e9
for i in range(1, n + 1):
  for v in combinations([i for i in range(n)], i):
    bitter = 1
    sour = 0
    for i in range(len(v)):
      bitter *= array[v[i]][0]
      sour += array[v[i]][1]
    min_value = min(min_value, abs(bitter - sour))

print(min_value)
