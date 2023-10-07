# https://www.acmicpc.net/problem/11660

import sys

input = sys.stdin.readline

n, m = map(int,input().split())

dp = [[0]*(n+1)]
for _ in range(n):
  dp.append([0]+list(map(int,input().split())))

for i in range(1,n+1):
  for j in range(2,n+1):
    dp[i][j] += dp[i][j-1] 
    
for i in range(1,n+1):
  for j in range(2,n+1):
    dp[j][i] += dp[j-1][i]

for _ in range(m):
  x1,y1,x2,y2 = map(int,input().split())
  print(dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1])