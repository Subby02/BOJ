# https://www.acmicpc.net/problem/2512

import sys

n = int(sys.stdin.readline())
array = list(map(int , sys.stdin.readline().split()))
m = int(sys.stdin.readline())

start = 0
end = max(array)

result = 0
while start <= end:
  mid = (start+end)//2
  
  total = 0
  for a in array:
    if a > mid:
      total+=mid
    else:
      total+=a
      
  if total > m:
    end = mid-1
  else:
    start = mid+1
    result = mid

print(result)
  