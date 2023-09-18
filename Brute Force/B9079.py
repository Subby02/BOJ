# https://www.acmicpc.net/problem/9079

import sys
from itertools import combinations

input = sys.stdin.readline

t = int(input())

change = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)],
          [(2, 0), (2, 1), (2, 2)], [(0, 0), (1, 0), (2, 0)],
          [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
          [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]


def solution():
  if isAll():
    return 0
  for i in range(1, 8):
    for p in combinations([i for i in range(8)], i):
      for c in p:
        reverseCoin(c)

      if isAll():
        return i

      for c in p:
        reverseCoin(c)

  return -1


def reverseCoin(n):
  for x, y in change[n]:
    if graph[x][y] == 'H':
      graph[x][y] = 'T'
    else:
      graph[x][y] = 'H'


def isAll():
  for i in range(3):
    for j in range(3):
      if graph[i][j] != graph[0][0]:
        return False

  return True


for _ in range(t):
  graph = []
  for _ in range(3):
    graph.append(input().rstrip().split())

  print(solution())
