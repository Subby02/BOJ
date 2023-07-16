# https://www.acmicpc.net/problem/12933

import sys

input = sys.stdin.readline

n = input().rstrip()

word = 'quack'
visited = [False] * len(n)

cnt = 0
for i in range(len(n)):
  if n[i] == 'q':
    k = 0
    fisrt = True
    for j in range(i, len(n)):
      if n[j] == word[k] and not visited[j]:
        visited[j] = True
        k += 1
      if k == 5:
        k = 0
        if fisrt:
          cnt += 1
          fisrt = False

if False in visited or len(n) % 5 != 0 or cnt == 0:
  print(-1)
else:
  print(cnt)
