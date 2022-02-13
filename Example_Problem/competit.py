from collections import deque

n, k = map(int,input().split())
graph = []
virus = []
for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    if graph[i][j] != 0:
      virus.append((graph[i][j],0,i,j))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

virus.sort()
q = deque(virus)

s, x, y = map(int, input().split()) #time, (x,y)

while q:
  v, v_s, v_x, v_y = q.popleft()
  if s == v_s:
    break
  for i in range(4):
    nx = v_x+dx[i]
    ny = v_y+dy[i]
    if 0 <= nx and nx<n and 0<=ny and ny<n:
      if graph[nx][ny] == 0:
        graph[nx][ny] = v
        q.append((v, v_s+1, nx, ny))

print(graph[x-1][y-1])
