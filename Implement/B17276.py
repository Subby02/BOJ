# https://www.acmicpc.net/problem/17276

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n, d = map(int, input().split())
  graph = []
  for _ in range(n):
    graph.append(input().rstrip().split())

  if d < 0:
    d += 360

  for _ in range(d // 45):
    temp = []
    for i in range(n):
      temp.append(graph[i][n - 1 - i])
      graph[i][n - 1 - i] = graph[i][n // 2]

    for i in range(n):
      graph[n // 2][n - 1 - i], temp[i] = temp[i], graph[n // 2][n - 1 - i]

    for i in range(n):
      graph[n - 1 - i][n - 1 - i], temp[i] = temp[i], graph[n - 1 - i][n - 1 -
                                                                       i]

    for i in range(n):
      graph[n - 1 - i][n // 2] = temp[i]

  for v in graph:
    print(' '.join(v))
