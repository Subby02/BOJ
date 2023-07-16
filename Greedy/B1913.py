# https://www.acmicpc.net/problem/1913

import sys

input = sys.stdin.readline

n = int(input())

m = int(input())

graph = [[0] * (n + 1) for _ in range(n + 1)]

x = n // 2 + 1
y = n // 2 + 1
cnt = 1
graph[x][y] = cnt

tx = x
ty = y
for i in range(3, n + 1, 2):
  x -= 1
  graph[x][y] = cnt
  cnt += 1
  if cnt == m:
    tx = x
    ty = y
  for _ in range(i - 2):
    graph[x][y] = cnt
    cnt += 1
    y += 1
    if cnt == m:
      tx = x
      ty = y
  for _ in range(i - 1):
    graph[x][y] = cnt
    cnt += 1
    x += 1
    if cnt == m:
      tx = x
      ty = y
  for _ in range(i - 1):
    graph[x][y] = cnt
    cnt += 1
    y -= 1
    if cnt == m:
      tx = x
      ty = y
  for _ in range(i - 1):
    graph[x][y] = cnt
    cnt += 1
    x -= 1
    if cnt == m:
      tx = x
      ty = y
  graph[x][y] = cnt

for v in graph[1:]:
  for v2 in v[1:]:
    print(v2, end=' ')
  print()

print(tx, ty)
