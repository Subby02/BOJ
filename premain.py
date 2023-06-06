# 코딩테스트 할 때 필수적인 라이브러리와 함수가 저장된 py

import sys 
import heapq #우선순위 큐 , 다익스트라
from collections import deque #큐 , bfs
from itertools import combinations , permutations #브루트 포스
from bisect import bisect_left , bisect_right #이분탐색

input = sys.stdin.readline
sys.setrecursionlimit(10000) # 재귀 한도

# =============== BFS , DFS ===============
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

def bfs(start):
  q = deque()
  q.append(start)
  visited[start] = True

  while q:
    now = q.popleft()
    print(now, end=' ')

    for i in graph[now]:
      if not visited[i]:
        visited[i] = True
        q.append(i)

def dfs(start):
  visited[start] = True
  print(start, end=' ')

  for i in graph[start]:
    if not visited[i]:
      dfs(i)

# =============== 이분탐색 ===============
def bs(array , target):
  start = 0
  end = max(array)

  while start <= end:
    mid = (start+end) // 2
    if array[mid] == target:
      return mid
    elif total > target:
      start = mid+1
    else:
      end = mid-1

  return end

# =============== 다익스트라 ===============
graph = [[] for i in range(d + 1)]
distance = [INF] * (d + 1)

def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    dist , now = heapq.heappop(q)

    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

# =============== 플루이드 위셜 ===============
for k in range(n):
  for i in range(n):
    for j in range(n):
      dp[i][j] = min(dp[i][j] , dp[i][k]+dp[k][j])