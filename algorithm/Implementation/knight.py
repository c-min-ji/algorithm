position = input()

row = int(position[1]) #row가 세로로 숫자적혀있는 그 부분 볼 거
column = int(ord(position[0]))-int(ord('a')) + 1 #문자를 ord로 변환해 숫자로 받아 줌 그리고 a-a 하면 0 되니까 +1해준다

step = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)] #1번 => (오, 위), (오, 아래), (왼, 위), (왼, 아래) 2번=> ((오, 위), (오, 아래), (왼, 위), (왼, 아래)

result = 0 #몇 번 옮길 수 있는 지 계산
for st in step:
  next_row = row+st[1] #이건 st[0]이든 st[1]이든 상관없을 듯
  next_col = column+st[0] #이건 st[0]이든 st[1]이든 상관없을 듯
  if next_row >= 1 and next_col >= 1 and next_row <= 8 and next_col <= 8: #위치가 1<= 위치 <= 8 이면 카운팅
    result += 1
    
print(result)
