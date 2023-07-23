# https://www.acmicpc.net/problem/16508

from itertools import combinations
import sys

input = sys.stdin.readline

t = input().rstrip()

n = int(input())

array = []
for _ in range(n):
  c, w = input().rstrip().split()
  array.append((int(c), list(w)))

min_cost = 1e9
for i in range(1, n + 1):
  for books in combinations(array, i):
    cost = 0
    str = []
    for book in books:
      cost += book[0]
      str += book[1]
    isPossible = True
    for c in t:
      if c in str:
        str.remove(c)
      else:
        isPossible = False
        break
    if isPossible:
      min_cost = min(min_cost, cost)

if min_cost == 1e9:
  print(-1)
else:
  print(min_cost)
