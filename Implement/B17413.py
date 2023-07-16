# https://www.acmicpc.net/problem/17413

import sys

input = sys.stdin.readline

str = input().rstrip()

newStr = ''
newWord = ''
isTag = False
for c in str:
  if c == '<':
    newStr += newWord[::-1] + c
    newWord = ''
    isTag = True
  elif c == '>':
    isTag = False
    newStr += c
  elif c == ' ':
    newStr += newWord[::-1] + ' '
    newWord = ''
  else:
    if isTag:
      newStr += c
    else:
      newWord += c
newStr += newWord[::-1]

print(newStr)
