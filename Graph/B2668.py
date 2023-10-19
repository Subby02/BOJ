# https://www.acmicpc.net/problem/2668

import sys

input = sys.stdin.readline

n = int(input())

array = [0]

for _ in range(n):
  array.append(int(input()))


def dfs(i):
  visited = []
  q = []
  q.append(i)

  while q:
    x = q.pop()

    if x not in visited:
      visited.append(x)

      q.append(array[x])

  return x == i


cnt = 0
result = []
for i in range(1, n + 1):
  if dfs(i):
    cnt += 1
    result.append(i)

print(cnt)
for v in result:
  print(v)
