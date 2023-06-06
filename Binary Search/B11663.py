# https://www.acmicpc.net/problem/11663

import sys

input = sys.stdin.readline

n, m = map(int , input().split())

point = list(map(int,input().split()))
point.sort()

def left_bs(array, target):
  start = 0
  end = len(array)-1
  while start <= end:
    mid = (start+end)//2
    if target > array[mid]:
      start = mid+1
    else:
      end = mid-1
  
  return end+1

def right_bs(array, target):
  start = 0
  end = len(array)-1
  while start <= end:
    mid = (start+end)//2
    if target >= array[mid]:
      start = mid+1
    else:
      end = mid-1
  
  return end

for _ in range(m):
  x, y = map(int , input().split())
  result = right_bs(point , y) - left_bs(point , x) + 1
  print(result)