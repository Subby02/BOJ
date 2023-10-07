# https://www.acmicpc.net/problem/2346

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

array = list(map(int,input().split()))

q = deque()
for i in range(n):
  q.append((i+1,array[i]))

while q:
  i,v = q.popleft()
  print(i,end=' ')

  if not q:
    break

  if v > 0:
    for _ in range(v-1):
      q.append(q.popleft())
  else:
    for _ in range(-v):
      q.appendleft(q.pop())