# https://www.acmicpc.net/problem/13305

import sys

input = sys.stdin.readline

n = int(input())

city = list(map(int , input().split()))
gas = list(map(int , input().split()))

min_gas = 1e9

total = 0
for i in range(n-1):
  min_gas = min(min_gas , gas[i])
  total += city[i] * min_gas

print(total)