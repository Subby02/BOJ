# https://www.acmicpc.net/problem/2470

import sys

input = sys.stdin.readline

n = int(input())

array = list(map(int,input().split()))

array.sort()

left = 0
right = n-1
result = 2000000001
temp = (0,n-1)

while left < right:
  sum = array[left] + array[right]

  if abs(sum) < result:
    result = abs(sum)
    temp = (left,right)

  if sum == 0:
    break
  elif sum > 0:
    right -= 1
  else:
    left += 1

print(array[temp[0]] , array[temp[1]])