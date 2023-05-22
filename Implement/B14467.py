# https://www.acmicpc.net/problem/14467

import sys

input = sys.stdin.readline

n = int(input())

cow = [-1] * 10

cnt = 0
for _ in range(n):
  a , b = map(int , input().split())
  if cow[a-1] == -1:
    cow[a-1] = b
  else:
    if cow[a-1] != b:
      cnt+=1
    cow[a-1] = b

print(cnt)