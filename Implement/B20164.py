# https://www.acmicpc.net/problem/20164

import sys

input = sys.stdin.readline

result = []

def countOdd(n):
  n = list(map(int,str(n)))

  cnt = 0
  for v in n:
    if v % 2 == 1:
      cnt += 1

  return cnt

def slice(n,i,j):
  n = str(n)
  total = int(n[:i]) + int(n[i:j]) + int(n[j:])

  return total

def re(n,cnt):
  length = len(str(n))
  if length == 1:
    result.append(cnt)

  elif length == 2:
    n = n//10 + n%10
    cnt += countOdd(n)
    re(n,cnt)
  else:
    for i in range(1,length-1):
      for j in range(i+1,length):
        newN = slice(n,i,j)
        re(newN,cnt+countOdd(newN))

n = int(input())

re(n,countOdd(n))
print(min(result),max(result))