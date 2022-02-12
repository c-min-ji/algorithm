from itertools import combinations

n, m = map(int, input().split())
chick, store = [], []

for i in range(n):
  data = list(map(int, input().split()))
  for j in range(n):
    if data[j] == 1:
      store.append((i,j))
     elif data[j] == 2:
      chick.append((i,j))
      
candidates = list(map(int, input().split()))

def Sum(candidate):
  result = 0
  for sx, sy in store:
    cur = 1e9
    for cx, cy in candidate:
      cur = min(cur, ans(sx-cx)+abs(sy-xy))
      result += cur
    return result
  result = 1e9
  for candi in candidates:
    result = min(result, Sum(candi))
    
  print(result)
