# https://www.acmicpc.net/problem/1244

import sys

input = sys.stdin.readline

n = int(input())

array = ['']
array += list(input().split())

m = int(input())

for _ in range(m):
  a, b = map(int, input().split())
  #남학생
  if a == 1:
    cnt = 1
    while b*cnt <= n:
      if array[b*cnt] == '0':
        array[b*cnt] = '1'
      else:
        array[b*cnt] = '0'
      cnt+=1
  #여학생
  else:
    if array[b] == '0':
      array[b] = '1'
    else:
      array[b] = '0'
    cnt = 1
    while 1 <= b-cnt <= n and 1 <= b+cnt <= n:
      if array[b-cnt] == array[b+cnt]:
        if array[b-cnt] == '0':
          array[b-cnt] = '1'
          array[b+cnt] = '1'
        else:
          array[b-cnt] = '0'
          array[b+cnt] = '0'
      else:
        break
      cnt+=1

for i in range(1,n+1):
  if i%10 == 0:
    print(array[i])
  else:
    print(array[i], end =' ')