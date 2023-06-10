# https://www.acmicpc.net/problem/20436

import sys

input = sys.stdin.readline

left_keyboard = [['q','w','e','r','t'],['a','s','d','f','g'],['z','x','c','v']]
right_keyboard = [['y','u','i','o','p'],['h','j','k','l'],['b','n','m']]

pos = {}

for i in range(3):
  j = 0
  for key in left_keyboard[i]:
    pos[key] = (i,j)
    j+=1
  for key in right_keyboard[i]:
    pos[key] = (i,j)
    j+=1

def isLeft(n):
  for v in left_keyboard:
    if n in v:
      return True
  return False

sl , sr = input().rstrip().split()

str = input().rstrip()

second = len(str)

for s in str:
  if isLeft(s):
    x , y = pos[sl]
    nx , ny = pos[s]
    second += abs(x-nx)+abs(y-ny)
    sl = s
  else:
    x , y = pos[sr]
    nx , ny = pos[s]
    sr = s
    second += abs(x-nx)+abs(y-ny)

print(second)