h = int(input())

cnt = 0

for hour in range(h+1): # 0일 때, 1일 때, 2일 때, 3일 때 해야하니까 +1해준다
  for i in range(60): #분
    for j in range(60): #초
      if '3' in str(hour) + str(i) + str(j): #문자열에서 3이있으면 +1
        cnt += 1
print(cnt)
