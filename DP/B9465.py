# https://www.acmicpc.net/problem/9465

import sys

input = sys.stdin.readline

t = int(input())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(t):
  n = int(input())
  array = []
  
  for _ in range(2):
    array.append(list(map(int,input().split())))

  if n != 1:
    array[0][1] += array[1][0]
    array[1][1] += array[0][0]
    
    for i in range(2,n):
      array[0][i] += max(array[1][i-1],array[1][i-2])
      array[1][i] += max(array[0][i-1],array[0][i-2])

  print(max(array[0][-1],array[1][-1]))