# https://www.acmicpc.net/problem/13549

# dirty
import sys
import heapq
input = sys.stdin.readline

n, k= map(int, input().split())

INF = 1e9
graph = [[] for _ in range(100001)]
distance = [INF] * (100001)

for i in range(100001):
  if i == 0:
    graph[i].append((i+1,1))
  elif i == 100000:
    graph[i].append((i-1,1))
  else:
    graph[i].append((i-1,1))
    graph[i].append((i+1,1))
  if 2*i <= 100000:
    graph[i].append((2*i,0))

def dijkstra(start):
  q = []
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    dist , now = heapq.heappop(q)

    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))


dijkstra(n)

print(distance[k])

# clean
import sys
import heapq
input = sys.stdin.readline

n, k= map(int, input().split())
INF = 1e9

def dijkstra(N,K):
    distance = [INF]*(100001)
    distance[N] =0 
    hq = []
    heapq.heappush(hq,(0,N))
    while hq:
        dist,n = heapq.heappop(hq)
        for nx in [(n+1,1),(n-1,1),(n*2,0)]:
            if 0<=nx[0]<=100000 and distance[nx[0]] > dist + nx[1]:
                distance[nx[0]] = dist + nx[1]
                heapq.heappush(hq,(distance[nx[0]],nx[0]))
    print(distance[K])
  
dijkstra(n,k)