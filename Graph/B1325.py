# https://www.acmicpc.net/problem/1325

import sys
from collections import deque

input = sys.stdin.readline

n, m= map(int , input().split())

graph = [[] for _ in range(n+1)] 

for _ in range(m):
  a, b = map(int , input().split())

  graph[b].append(a)

def bfs(start):
  visited = [False for _ in range(n+1)]
  cnt = 1
  q = deque()
  q.append(start)
  visited[start] = True
  while q:
    now = q.popleft()
        
    for i in graph[now]:
      if not visited[i]:
        cnt+=1
        visited[i] = True
        q.append(i)
        
  return cnt

array = []
for i in range(1,n+1):
  array.append(bfs(i))

max_cnt = max(array)
for i in range(n):
  if array[i] == max_cnt:
    print(i+1 , end=' ')