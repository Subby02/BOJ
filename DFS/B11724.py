# https://www.acmicpc.net/problem/11724

import sys

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(m):
  u , v = map(int, sys.stdin.readline().split())

  graph[u].append(v)
  graph[v].append(u)

cnt = 0
for i in range(1,n+1):
  if not visited[i]:
    cnt += 1
    
    stack = []
    stack.append(i)
    visited[i] = True
  
    while stack:
      now = stack.pop()
  
      for j in graph[now]:
        if not visited[j]:
          visited[j] = True
          stack.append(j)

print(cnt)