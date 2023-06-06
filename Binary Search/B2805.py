# https://www.acmicpc.net/problem/2805

import sys

input = sys.stdin.readline

n, m = map(int , input().split())

array = list(map(int,input().split()))
array.sort()

def bs(array , target):
  start = 0
  end = max(array)

  while start <= end:
    mid = (start+end) // 2
    total = 0
    
    for v in array:
      if v > mid:
        total += v-mid
    if total == target:
      return mid
    elif total > target:
      start = mid+1
    else:
      end = mid-1

  return end

print(bs(array,m))