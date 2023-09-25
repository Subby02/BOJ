# https://www.acmicpc.net/problem/1158

import sys
from collections import deque

input = sys.stdin.readline

n, k= map(int,input().split())

result = []
q = deque([i for i in range(1,n+1)])
while q:
  for _ in range(k-1):
    q.append(q.popleft())
    
  result.append(q.popleft())

  
print('<'+', '.join(map(str,result))+'>')
