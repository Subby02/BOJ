# https://www.acmicpc.net/problem/1654

import sys

input = sys.stdin.readline

k, n = map(int, input().split())

array = []
for _ in range(k):
  array.append(int(input()))

result = 0
start = 1
end = max(array)
while start <= end:
  mid = (start + end) // 2

  cnt = 0
  for v in array:
    cnt += v // mid

  if cnt >= n:
    result = mid
    start = mid + 1
  else:
    end = mid - 1

print(result)
