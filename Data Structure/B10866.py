# https://www.acmicpc.net/problem/10866

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

q = deque()
for _ in range(n):
  args = input().rstrip().split()
  
  if args[0] == "push_front":
    q.appendleft(int(args[1]))
  elif args[0] == "push_back":
    q.append(int(args[1]))
  elif args[0] == "pop_front":
    if not q:
      print(-1)
    else:
      print(q.popleft())
  elif args[0] == "pop_back":
    if not q:
      print(-1)
    else:
      print(q.pop())
  elif args[0] == "size":
    print(len(q))
  elif args[0] == "empty":
    if not q:
      print(1)
    else:
      print(0)
  elif args[0] == "front":
    if not q:
      print(-1)
    else:
      print(q[0])
  elif args[0] == "back":
    if not q:
      print(-1)
    else:
      print(q[-1])
    