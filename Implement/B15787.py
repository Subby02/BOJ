# https://www.acmicpc.net/problem/15787

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
trains = [[False] * 21 for _ in range(n + 1)]

for _ in range(m):
  args = list(map(int, input().split()))

  if args[0] == 1:
    trains[args[1]][args[2]] = True
  elif args[0] == 2:
    trains[args[1]][args[2]] = False
  elif args[0] == 3:
    for i in range(19, 0, -1):
      trains[args[1]][i + 1] = trains[args[1]][i]
    trains[args[1]][1] = False
  elif args[0] == 4:
    for i in range(2, 21):
      trains[args[1]][i - 1] = trains[args[1]][i]
    trains[args[1]][20] = False

filter = []
for t in trains[1:]:
  if t[1:] not in filter:
    filter.append(t[1:])

print(len(filter))
