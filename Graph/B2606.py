# https://www.acmicpc.net/problem/2606

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)] 

for _ in range(m):
  a, b = map(int , input().split())

  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (n+1)

def bfs(start):
  q = deque()
  q.append(start)
  visited[start] = True
  while q:
    now = q.popleft()
        
    for i in graph[now]:
      if not visited[i]:
        visited[i] = True
        q.append(i)

bfs(1)
print(visited.count(True)-1)