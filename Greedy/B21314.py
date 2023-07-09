# https://www.acmicpc.net/problem/21314

import sys

input = sys.stdin.readline

n = input().rstrip()

max_str = ''
min_str = ''
cnt = 0
for s in n:
  if s == 'M':
    cnt += 1
  elif s == 'K':
    if cnt == 0:
      min_str += '5'
    else:
      min_str += str(10**(cnt - 1)) + '5'
    max_str += str(10**cnt * 5)
    cnt = 0

if cnt != 0:
  max_str += '1' * cnt
  min_str += str(10**(cnt - 1))

print(max_str)
print(min_str)
