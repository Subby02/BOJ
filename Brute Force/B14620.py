# https://www.acmicpc.net/problem/14620

import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

array = []
for _ in range(n):
  array.append(list(map(int, input().split())))

result = []
for combi in combinations([(i,j) for i in range(1,n-1) for j in range(1,n-1)],3):
  visited = [[0] * n for _ in range(n)]
  for x,y in combi:
    visited[x][y] += 1

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      visited[nx][ny] += 1

  isFail = False
  value = 0
  for x in range(n):
    for y in range(n):
      if visited[x][y] == 1:
        value += array[x][y]
      if visited[x][y] > 1:
        isFail = True

  if not isFail:
    result.append(value)
      
print(min(result))