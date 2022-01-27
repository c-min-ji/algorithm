from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))
  
  
dx = [-1, 1, 0, 0]
