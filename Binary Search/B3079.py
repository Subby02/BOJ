# https://www.acmicpc.net/problem/3079

import sys

input = sys.stdin.readline

n, m = map(int,input().split())

array = []
for _ in range(n):
  array.append(int(input()))

array.sort()

start = 0
end = array[-1]*m
while start <= end:
  mid = (start+end)//2
  
  total = 0
  for v in array:
    total += mid//v
    
  if total >= m:
    end = mid-1
    result = mid
  else:
    start = mid+1

print(result)