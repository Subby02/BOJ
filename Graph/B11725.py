# https://www.acmicpc.net/problem/11725

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)] 

for _ in range(n-1):
  a, b = map(int , input().split())

  graph[a].append(b)
  graph[b].append(a)

root = [0] * (n+1)

def bfs(start):
  q = deque()
  q.append(start)
  root[start] = 1
  while q:
    now = q.popleft()
        
    for i in graph[now]:
      if root[i] == 0:
        root[i] = now
        q.append(i)

bfs(1)
for v in root[2:]:
  print(v)
  