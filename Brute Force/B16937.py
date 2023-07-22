# https://www.acmicpc.net/problem/16937

import sys

input = sys.stdin.readline

h, w = map(int, input().split())

n = int(input())

array = []

max_length = max(h, w)

for _ in range(n):
  r, c = map(int, input().split())
  array.append((r, c))

result = 0
for i in range(n):
  for j in range(i + 1, n):
    r1, c1 = array[i]
    r2, c2 = array[j]

    if (r1 + r2 <= h and max(c1, c2) <= w) or (max(r1, r2) <= h
                                               and c1 + c2 <= w):
      result = max(result, r1 * c1 + r2 * c2)
    if (c1 + r2 <= h and max(r1, c2) <= w) or (max(c1, r2) <= h
                                               and r1 + c2 <= w):
      result = max(result, r1 * c1 + r2 * c2)
    if (c1 + c2 <= h and max(r1, r2) <= w) or (max(c1, c2) <= h
                                               and r1 + r2 <= w):
      result = max(result, r1 * c1 + r2 * c2)
    if (r1 + c2 <= h and max(c1, r2) <= w) or (max(r1, c2) <= h
                                               and c1 + r2 <= w):
      result = max(result, r1 * c1 + r2 * c2)

print(result)