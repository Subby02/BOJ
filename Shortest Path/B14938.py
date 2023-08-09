# https://www.acmicpc.net/problem/14938

import sys

input = sys.stdin.readline

n,m,r = map(int, input().split())

items = [0]
items += list(map(int,input().split()))

INF = 1e9
graph = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(r):
  a,b,l = map(int, input().split())
  graph[a][b] = l
  graph[b][a] = l

for i in range(1,n+1):
  graph[i][i] = 0

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j] = min(graph[i][j] , graph[i][k] + graph[k][j])

max_total = 0
for i in range(1,n+1):
  total = 0
  for j in range(1,n+1):
    if graph[i][j] <= m:
      total += items[j]
  max_total = max(max_total , total)

print(max_total)