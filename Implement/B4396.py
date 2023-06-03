# https://www.acmicpc.net/problem/4396

import sys

input = sys.stdin.readline

n = int(input())

mine = []
player =  []

dpos = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

for _ in range(n):
  mine.append(list(input().rstrip()))

for _ in range(n):
  player.append(list(input().rstrip()))

isFail = False
for i in range(n):
  for j in range(n):
    if player[i][j] == 'x':
      if mine[i][j] == '*':
        isFail = True
      else:
        cnt = 0
        for k in range(8):
          nx = i + dpos[k][0]
          ny = j + dpos[k][1]
    
          if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
          if mine[nx][ny] == '*':
            cnt+=1
        player[i][j] = str(cnt)

if isFail:
  for i in range(n):
    for j in range(n):
      if mine[i][j] == '*':
        player[i][j] = '*'

for v in player:
  print(''.join(v))