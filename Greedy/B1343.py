# https://www.acmicpc.net/problem/1343

import sys

board = sys.stdin.readline().rstrip()

str = ''
cnt = 0
for c in board:
  if c == 'X':
    cnt+=1
    if cnt == 4:
      cnt = 0
      str += 'AAAA'
  else:
    if cnt != 0:
      if cnt == 2:
        cnt = 0
        str += 'BB'
      else:
        str = '-1'
        break
    str += '.'

if cnt != 0:
  if cnt == 4:
    cnt = 0
    str += 'AAAA'
  elif cnt == 2:
    cnt = 0
    str += 'BB'
  else:
    str = '-1'

print(str)