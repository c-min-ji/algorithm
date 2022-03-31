def DFS(graph, v, visited):
  visited[v] = True #v가 현재 노드니까 방문했다고 True로 변경
  print(v, end=" ") #출력 시: 1 2 3,,,과 같은 형태로 출력됨
  for i in graph[v]: #v와 인접한 노드동안
    if not visited[i]: #인접 노드가 방문되지 않았으면
      DFS(graph, i, visited) #재귀로 돈다
      
graph = [
  [],
  [2,3,8], #1번 노드와 인접한 노드
  [1,7], #2번 노드와 인접한 노드
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False]*9 #방문 표시하려고

DFS(graph, 1, visited)
