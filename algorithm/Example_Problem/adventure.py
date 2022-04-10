n = int(input())
x = list(map(int, input().split()))
max_x = max(x)
cnt = 0
group = 0
x.sort() #작은 것부터 봐야지 많이 할 수 있음 만약에 6개 중에 6이 젤 큰데 6부터 세면 하나밖에 못만듦
for i in x:
  cnt += 1
  if cnt >= i: 
    group+=1
    cnt = 0

print(group)
