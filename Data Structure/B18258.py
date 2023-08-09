# https://www.acmicpc.net/problem/18258

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

array = deque()

for _ in range(n):
  args = input().rstrip().split()

  if args[0] == 'push':
    array.append(args[1])
  elif args[0] == 'pop':
    if not array:
      print(-1)
    else:
      print(array.popleft())
  elif args[0] == 'size':
    print(len(array))
  elif args[0] == 'empty':
    if array:
      print(0)
    else:
      print(1)
  elif args[0] == 'front':
    if not array:
      print(-1)
    else:
      print(array[0])
  elif args[0] == 'back':
    if not array:
      print(-1)
    else:
      print(array[-1])