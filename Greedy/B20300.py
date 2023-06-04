# https://www.acmicpc.net/problem/20300

import sys
input = sys.stdin.readline

n = int(input())

array = list(map(int,input().split()))

array.sort()

length = len(array)
if length % 2 == 0:
  value = []
  for i in range(length//2):
    value.append(array[i] + array[length-i-1])
  print(max(value))
else:
  value = []
  value.append(array.pop(-1))
  for i in range((length-1)//2):
    value.append(array[i] + array[length-i-2])
  print(max(value))