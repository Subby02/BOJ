# https://www.acmicpc.net/problem/1874

import sys

input = sys.stdin.readline

n = int(input())

def solution():
  cnt = 1
  msg = []
  stack = []
  for _ in range(n):
    t = int(input())
    while not stack or t != stack[-1]:
      if cnt == n+1 and t != stack[-1]:
        msg = ['NO']
        return msg
      stack.append(cnt)
      msg.append('+')
      cnt += 1

    stack.pop()
    msg.append('-')

  return msg

msg = solution()
  
for s in msg:
  print(s)