# https://www.acmicpc.net/problem/2309

import sys
from itertools import combinations

array = []
for _ in range(9):
  array.append(int(sys.stdin.readline()))

for v in combinations(array , 7):
  if sum(v) == 100:
    for i in sorted(v):
      print(i)
    break