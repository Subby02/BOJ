# https://www.acmicpc.net/problem/1092

import sys

input = sys.stdin.readline

n = int(input())

crains = list(map(int,input().split()))

m = int(input())

weights = list(map(int,input().split()))

def solutions():
  crains.sort(reverse=True)
  weights.sort(reverse=True)

  if max(weights) > max(crains):
    return -1

  time = 0
  while weights:
    for c in crains:
      for w in weights:
        if w <= c:
          weights.remove(w)
          break
    time += 1

  return time

print(solutions())