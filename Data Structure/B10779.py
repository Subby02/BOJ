# https://www.acmicpc.net/problem/10799

import sys

input = sys.stdin.readline

array = list(input().rstrip())

plate = 0
total = 0
while array:
  if len(array) > 1:
    if array[-1] == ')' and array[-2] == '(':
      total+=plate
      array.pop()
      array.pop()
    elif array[-1] == ')':
      plate += 1
      array.pop()
    elif array[-1] == '(':
      plate -= 1
      total += 1
      array.pop()
  else:
    plate -= 1
    total += 1
    array.pop()

print(total)
    