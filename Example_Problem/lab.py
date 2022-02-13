n,m = map(int, input().split())
graph = []
wall = [[0]*m for _ in range(n)]
for _ in range(n):
  graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def virus(x, y):
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]

    if nx>= 0 and nx<n and ny >= 0 and ny < m:
      if wall[nx][ny] == 0:
        wall[nx][ny] = 2
        virus(nx, ny)

def get_score():
  score = 0
  for i in range(n):
    for j in range(m):
      if wall[i][j] == 0:
        score += 1
  return score

def dfs(cnt):
  global result
  if cnt == 3:
    for i in range(n):
      for j in range(m):
        wall[i][j] = graph[i][j]
    
    for i in range(n):
      for j in range(m):
        if wall[i][j] == 2:
          virus(i, j)

    result = max(result, get_score())
    return 
  
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        graph[i][j] = 1
        cnt += 1
        dfs(cnt)
        graph[i][j] = 0
        cnt -=1

dfs(0)
print(result)
