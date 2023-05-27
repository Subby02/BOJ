# https://www.acmicpc.net/problem/18312

import sys

input = sys.stdin.readline

n,k = map(int,input().split())

cnt = 0
for hour in range(0,n+1):
  for minute in range(0,60):
    for second in range(0,60):
      if str(k) in str(hour).zfill(2) or str(k) in str(minute).zfill(2) or str(k) in str(second).zfill(2):
        cnt += 1

print(cnt)