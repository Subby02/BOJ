# https://www.acmicpc.net/problem/1753

import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())

k = int(input())

graph = [[] for _ in range(V + 1)]
distance = [1e9] * (V + 1)

for _ in range(E):
  u, v, w = map(int, input().split())

  graph[u].append((v, w))


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


dijkstra(k)

for i in range(1, V + 1):
  if distance[i] == 1e9:
    print('INF')
  else:
    print(distance[i])
