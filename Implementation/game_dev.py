n, m = map(int, input().split())

d = [[0]* m for _ in range(n)]

x, y, direct = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
  array.append(list(map(int, input().split())))
  
dx = [-1, 0, 1, 0]  #북동남서(0123)
dy = [0, 1, 0, -1]

def turn_left():
  global direct
  direct -= 1
  if direct == -1:
    direct = 3

cnt = 1 #처음 시작 카운트
turn = 0 #회전

while True:
  turn_left()
  nx=x+dx[direct]
  ny=y+dy[direct]
  
  if d[nx][ny] === 0 and array[nx][ny] == 0:
    n[nx][ny] = 1
    x = nx
    y = ny
    cnt += 1
    continue
  else:
    turn +=1
  if turn == 4:
    nx = x - dx[direct]
    ny = y - dy[direct]
    if array[nx][ny] == 0:
      x = nx
      y = ny
    else:
      break
    turn = 0

print(cnt)
  
