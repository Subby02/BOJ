# https://www.acmicpc.net/problem/21608

import sys

input = sys.stdin.readline

n = int(input())

dx = [1,-1,0,0]
dy = [0,0,1,-1]
graph = [[0] * (n+1) for _ in range(n+1)]

array = []
for _ in range(n**2):
  array.append(list(map(int,input().split())))

for v in array:
  check = []
  student = v[0]
  friends = v[1:]
    
  for i in range(1, n+1):
    for j in range(1, n+1):
      if graph[i][j] != 0:
        continue
      empty = 0
      friendly = 0
      for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if nx < 1 or nx > n or ny < 1 or ny > n:
          continue

        if graph[nx][ny] in friends:
          friendly += 1
        elif graph[nx][ny] == 0:
          empty += 1
      check.append((friendly,empty,(i,j)))
  check.sort(key=lambda x : (-x[0] , -x[1] , x[2]))  # key point
  graph[check[0][2][0]][check[0][2][1]] = student
            
total = 0
for i in range(1, n+1):
  for j in range(1, n+1):
    for v in array:
      if v[0] == graph[i][j]:
        cnt = 0
        for k in range(4):
          nx = i + dx[k]
          ny = j + dy[k]

          if nx < 1 or nx > n or ny < 1 or ny > n:
            continue

          if graph[nx][ny] in v[1:]:
            cnt+=1
        if cnt == 1:
          total += 1
        elif cnt == 2:
          total+=10
        elif cnt == 3:
          total+=100
        elif cnt == 4:
          total+=1000

print(total)