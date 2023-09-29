# https://www.acmicpc.net/problem/1890

import sys

input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
  graph.append(list(map(int,input().split())))

dp = [[0] * n for _ in range(n)]

def re(x,y):
  if x >= n or y >= n:
    return 0
  
  if x == n-1 and y == n-1:
    return 1

  if graph[x][y] == 0:
    return 0

  dist = graph[x][y]
  
  if dp[x][y] == 0:
    dp[x][y] = re(x+dist,y) + re(x,y+dist)

  return dp[x][y]

re(0,0)

print(dp[0][0])