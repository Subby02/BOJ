# https://www.acmicpc.net/problem/10994

import sys

input = sys.stdin.readline

n = int(input())

array = [[' '] * (400) for _ in range(400)]

x = (1+(n-1)*4)//2
y = (1+(n-1)*4)//2
array[x][y] = '*'

for i in range(2,n+1):
  x -= 2
  y -= 2
  length = (1+(i-1)*4)
  for j in range(length):
    array[x][y+j] = '*'
    array[x+j][y] = '*'
    array[x+length-1][y+j] = '*'
    array[x+j][y+length-1] = '*'

for i in array[:(1+(n-1)*4)]:
  for j in i[:(1+(n-1)*4)]:
    print(j,end='')
  print()
