from collections import deque

n, m, k, x = map(int, input().split())
graph =[[] for _ in range(n+1)]

for _ in range(m):
  num, cn = map(int, input().split())
  graph[num].append(cn)

distance = [-1]*(n+1)
distance[x] = 0 #출발도시
q = deque([x])
while q:
  curr = q.popleft()
  for next in graph[curr]:
    if distance[next] == -1:
      distance[next] = distance[curr] + 1
      q.append(next)

check = False
for i in range(1, n+1):
  if distance[i] == k:
    print(i)
    check = True

if check==False:
  print(-1)
