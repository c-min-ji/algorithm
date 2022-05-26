n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() #A는 오름차순 정렬
b.sort(reverse=True) #B는 내림차순 정렬

for i in range(k): #k번만큼만 실행
  if a[i]<b[i]: #b가 더 크면 교체
    a[i], b[i] = b[i], a[i]
  else:
    break
    
print(sum(a))
