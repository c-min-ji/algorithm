def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x] #경로 압축 기법을 사용함. 기본 서로소 집합 알고리즘과는 여기만 달라짐

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a<b:
    parent[b] = a
  else:
    parent[a] = b
    
v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
  parent[i] = i
  
for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)
  
print("각 원소가 속한 집합: ", end=" ")
for i in range(1, v+1):
  print(find_parent, i), end=" ")
  
print()

print("부모 테이블: ", end=" ")
for i in range(1, v+1):
  print(parent[i], end=" ")
