# https://www.acmicpc.net/problem/10815

import sys

input = sys.stdin.readline

n = int(input())

card = list(map(int, input().split()))
card.sort()

m = int(input())

number = list(map(int, input().split()))

def bs(array, target, start, end):
  if start > end:
    return 0
  mid = (start+end)//2
  if array[mid] == target:
    return 1
  elif array[mid] > target:
    return bs(array,target,start,mid-1)
  else:
    return bs(array,target,mid+1,end)

for num in number:
  print(bs(card,num,0,len(card)-1),end=' ')