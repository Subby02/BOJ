# https://www.acmicpc.net/problem/11000

import sys
import heapq

input = sys.stdin.readline

n = int(input())

array = []
for _ in range(n):
  s, t = map(int,input().split())
  array.append((s,t))

array.sort()

room = []
heapq.heappush(room,array[0][1])

for i in range(1,n):
  if array[i][0] < room[0]:
    heapq.heappush(room,array[i][1])
  else:
    heapq.heappop(room)
    heapq.heappush(room,array[i][1])

print(len(room))