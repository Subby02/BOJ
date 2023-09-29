# https://www.acmicpc.net/problem/1277

import sys
import math
import heapq

input = sys.stdin.readline
INF = 1e9

n, w = map(int, input().split())

m = float(input())
distance = [INF] * (n + 1)

pos = [(-1, -1)]
for _ in range(n):
  x, y = map(int, input().split())
  pos.append((x, y))

graph = [[] for _ in range(n + 1)]
for x in range(1, n + 1):
  for y in range(x + 1, n + 1):
    cost = math.sqrt((pos[x][0] - pos[y][0])**2 + (pos[x][1] - pos[y][1])**2)
    if cost <= m:
      graph[x].append((y, cost))
      graph[y].append((x, cost))

for _ in range(w):
  a, b = map(int, input().split())

  graph[a].append((b, 0))
  graph[b].append((a, 0))


def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))


dijkstra(1)

print(int(distance[-1] * 1000))
