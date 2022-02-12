n = int(input())
board = [[0]*n for _ in range(n)]
k = int(input())
for _ in range(k):
  c, r = map(int, input().split())
  board[c-1][r-1] = 1

l = int(input())
L = []
for _ in range(l):
  sec, direct = input().split()
  L.append((int(sec), direct))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction, c):
  if c == 'L':
    direction = (direction-1)%4
  else:
    direction = (direction+1)%4

def solution():
  x, y = 1, 1
  board[x][y] = 2
  direction = 0
  time = 0
  index = 0
  q = [(x,y)]
  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 1 <= nx and nx <= n and 1 <= ny and ny <= n and board[nx][ny] != 2:
      if board[nx][ny] == 0:
        q.append((nx,ny))
        px, py = q.pop(0)
        board[px][py] = 0
      if board[nx][ny]==1:
        board[nx][ny] = 2
        q.append((nx,ny))
    else:
      time += 1
      break
    x,y = nx, ny
    time += 1
    if index<1 and time == board[index][0]:
      direction = turn(direction, board[index][1])
      index += 1
  return time

print(solution())
