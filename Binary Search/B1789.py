# https://www.acmicpc.net/problem/1789

import sys

input = sys.stdin.readline

s = int(input())

start = 0
end = s
while start <= end:
  mid = (start + end) // 2
  sum = mid * (mid + 1) / 2
  if sum > s:
    end = mid - 1
  else:
    start = mid + 1
    result = mid

print(result)
