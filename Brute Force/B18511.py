# https://www.acmicpc.net/problem/18511

import sys
from itertools import product

input = sys.stdin.readline

n, k = input().split()

array = input().split()

result = 0
for i in range(1,len(n)+1):
  for p in product(array, repeat=i):
    num = int(''.join(p))
    if num <= int(n):
      result = max(num,result)

print(result)