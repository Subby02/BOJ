# https://www.acmicpc.net/problem/1969

import sys

input = sys.stdin.readline

n, m = map(int,input().split())

array = []
for _ in range(n):
  array.append(input().rstrip())

result = ''
total = 0
for i in range(m):
  check = {'T':0,'A':0,'G':0,'C':0}
  for v in array:
    check[v[i]] += 1
  list = check.items()
  best = sorted(list,key=lambda x :(-x[1],x[0]))
  result += best[0][0]
  for v in array:
    if v[i] != best[0][0]:
      total += 1

print(result)
print(total)