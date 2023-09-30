# https://www.acmicpc.net/problem/1935

import sys

input = sys.stdin.readline

n = int(input())

s = list(input().rstrip())

array = []
for _ in range(n):
  array.append(int(input()))

stack = []
for i in s:
  if i.isalpha():
    stack.append(array[ord(i)-65])
  else:
    a=stack.pop()
    b=stack.pop()

    if i=='+':
      stack.append(b+a)

    elif i=='-':
      stack.append(b-a)

    elif i=='*':
      stack.append(b*a)

    elif i=='/':
      stack.append(b/a)
          
print('%0.2f'%stack[0])
