# https://www.acmicpc.net/problem/20291

import sys

input = sys.stdin.readline

n = int(input())

array = []

for _ in range(n):
  array.append(input().rstrip().split('.')[1])

array.sort()

cnt = 1
target = array[0]
for v in array[1:]:
  if v != target:
    print(target, cnt)
    target = v
    cnt = 1
  else:
    cnt += 1
print(target, cnt)
