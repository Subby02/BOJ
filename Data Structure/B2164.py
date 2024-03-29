# https://www.acmicpc.net/problem/2164

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

result = []
q = deque([i for i in range(1,n+1)])

while len(q) != 1:
  q.popleft()
  q.append(q.popleft())

print(q[0])
