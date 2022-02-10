n = int(input())
coin = list(map(int, input().split()))
coin.sort()

min_num = 1 #1보다 작은 수 없으면 바로 min_num 출력
for i in coin: #정렬되어있는 코인 리스트를 하나씩 돈다
  if min_num<i: #min_num이 i보다 작으면 만들 수 없는 거임! ex> 앞에꺼 다 더한 8이 9보다 작음 그러면 
    break
  min_num += i

print(min_num)
