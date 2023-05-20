# https://www.acmicpc.net/problem/19637

import sys

input = sys.stdin.readline
n, m = map(int , input().split())
title = []
power = []

def bs(p):
  start = 0
  end = len(power)-1

  res = 0
  while start <= end:
    mid = (start+end)//2
    if p > power[mid]:
      start = mid+1
    else:
      end = mid-1
      res = mid

  return res

for _ in range(n):
  a,b = input().split()
  title.append(a)
  power.append(int(b))

for _ in range(m):
  print(title[bs(int(input()))])