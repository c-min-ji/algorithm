def find_parent(parent, x):
  #루트 노드 찾을 때까지 재귀적으로 호출
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

#두 원소(a, b)가 속한 집합찾기
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
  
cycle = False

for i in range(e):
  a, b = map(int, input().split())
  if find_parent(parent, a) == find_parent(parent, b):
    cycle = True
    break
  else:
    union_parent(parent, a, b)
    
if cycle:
  print("cycle: True")
else:
  print("cycle: False")
