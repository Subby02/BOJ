# https://www.acmicpc.net/problem/19598

import sys
import heapq

input = sys.stdin.readline

n = int(input())

array = []
heap = []

for _ in range(n):
  start , end = map(int,input().split())
  array.append((start, end))

array.sort()

for start , end in array:
  if heap and heap[0] <= start:
    heapq.heappop(heap)
  heapq.heappush(heap,end)

print(len(heap))

      

