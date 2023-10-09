# https://www.acmicpc.net/problem/16926

import sys

input = sys.stdin.readline

n , m , r= map(int,input().split())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

array = []
for _ in range(n):
  array.append(list(map(int,input().split())))

for _ in range(r):
  for i in range(min(n,m)//2):
    x = i
    y = i
    temp = array[x][y]
    for _ in range(n-1-i*2):
      nx = x + dx[0]
      ny = y + dy[0]
   
      array[nx][ny] , temp = temp , array[nx][ny]

      x = nx
      y = ny

    for _ in range(m-1-i*2):
      nx = x + dx[1]
      ny = y + dy[1]

      array[nx][ny] , temp = temp , array[nx][ny]

      x = nx
      y = ny

    for _ in range(n-1-i*2):
      nx = x + dx[2]
      ny = y + dy[2]
      
      array[nx][ny] , temp = temp , array[nx][ny]

      x = nx
      y = ny

    for _ in range(m-1-i*2):     
      nx = x + dx[3]
      ny = y + dy[3]

      array[nx][ny] , temp = temp , array[nx][ny]

      x = nx
      y = ny

for v in array:
  print(*v)