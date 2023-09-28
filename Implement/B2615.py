# https://www.acmicpc.net/problem/2615

import sys

input = sys.stdin.readline

array = []
for _ in range(19):
  array.append(list(map(int, input().split())))


def solution():
  for x in range(19):
    for y in range(19):
      if array[x][y] != 0:
        target = array[x][y]

        # \
        cnt = 1
        for i in range(1, 6):
          nx = x - i
          ny = y - i

          if nx < 0 or nx >= 19 or ny < 0 or ny >= 19:
            break

          if array[nx][ny] == target:
            cnt += 1
          else:
            break

        mx = nx + 1
        my = ny + 1

        for i in range(1, 6):
          nx = x + i
          ny = y + i

          if nx < 0 or nx >= 19 or ny < 0 or ny >= 19:
            break

          if array[nx][ny] == target:
            cnt += 1
          else:
            break

        if cnt == 5:
          return target, mx, my

        # /
        cnt = 1
        for i in range(1, 6):
          nx = x - i
          ny = y + i

          if nx < 0 or nx >= 19 or ny < 0 or ny >= 19:
            break

          if array[nx][ny] == target:
            cnt += 1
          else:
            break

        for i in range(1, 6):
          nx = x + i
          ny = y - i

          if nx < 0 or nx >= 19 or ny < 0 or ny >= 19:
            break

          if array[nx][ny] == target:
            cnt += 1
          else:
            break

        mx = nx - 1
        my = ny + 1

        if cnt == 5:
          return target, mx, my

        # -
        cnt = 1
        for i in range(1, 6):
          nx = x
          ny = y - i

          if nx < 0 or nx >= 19 or ny < 0 or ny >= 19:
            break

          if array[nx][ny] == target:
            cnt += 1
          else:
            break

        mx = nx
        my = ny + 1

        for i in range(1, 6):
          nx = x
          ny = y + i

          if nx < 0 or nx >= 19 or ny < 0 or ny >= 19:
            break

          if array[nx][ny] == target:
            cnt += 1
          else:
            break

        if cnt == 5:
          return target, mx, my

        # |
        cnt = 1
        for i in range(1, 6):
          nx = x - i
          ny = y

          if nx < 0 or nx >= 19 or ny < 0 or ny >= 19:
            break

          if array[nx][ny] == target:
            cnt += 1
          else:
            break

        mx = nx + 1
        my = ny

        for i in range(1, 6):
          nx = x + i
          ny = y

          if nx < 0 or nx >= 19 or ny < 0 or ny >= 19:
            break

          if array[nx][ny] == target:
            cnt += 1
          else:
            break

        if cnt == 5:
          return target, mx, my

  return 0, -1, -1


winner, x, y = solution()

if winner == 0:
  print(winner)
else:
  print(winner)
  print(x + 1, y + 1)
