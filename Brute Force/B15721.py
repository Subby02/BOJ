# https://www.acmicpc.net/problem/15721

import sys

input = sys.stdin.readline

def solution():
  a = int(input())
  t = int(input())
  b = int(input())
  
  pattern = [0,1,0,1]
  array = []
  
  cnt = 2
  while True:
    for v in pattern:
      array.append(v)
      if array.count(b) == t:
        return (len(array)-1)%a
    for _ in range(cnt):
      array.append(0)
      if array.count(b) == t:
        return (len(array)-1)%a
    for _ in range(cnt):
      array.append(1)
      if array.count(b) == t:
        return (len(array)-1)%a
    cnt+=1

print(solution())