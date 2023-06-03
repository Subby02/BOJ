# https://www.acmicpc.net/problem/2578

import sys

input = sys.stdin.readline

graph = [(-1,-1)] * 26
check = [[False] * 5 for _ in range(5)]
turn = []
bingo = []

for x in range(5):
  array = list(map(int, input().split()))
  for y in range(5):
    graph[array[y]] = (x,y)

for _ in range(5):
  turn += list(map(int, input().split()))

for i in range(25):
  x = graph[turn[i]][0]
  y = graph[turn[i]][1]
  check[x][y] = True
  
  isBingo = True
  if (0,y) not in bingo:
    for j in range(5):
      if not check[j][y]:
        isBingo = False
        break
    if isBingo:
      bingo.append((0,y))
      if len(bingo) == 3:
        print(i+1)
        break
  isBingo = True
  if (x,0) not in bingo:
    for j in range(5):
      if not check[x][j]:
        isBingo = False
        break
    if isBingo:
      bingo.append((x,0))
      if len(bingo) == 3:
        print(i+1)
        break
  isBingo = True
  if (2,2) not in bingo:
    for j in range(5):
      if not check[j][j]:
        isBingo = False
        break
    if isBingo:
      bingo.append((2,2))
      if len(bingo) == 3:
        print(i+1)
        break

  isBingo = True
  if (-2,-2) not in bingo:
    for j in range(5):
      if not check[j][4-j]:
        isBingo = False
        break
    if isBingo:
      bingo.append((-2,-2))
      if len(bingo) == 3:
        print(i+1)
        break
  
  