from collections import deque

def bfs(graphs, v, visited):
  queue  = deque()
  visited = True #방문한 거 True 처리
  while queue: #queue가 없어질 때까지
    v = queue.popleft() #제일 먼저 들어온 거 없애고
    print(v, end=" ") #출력: 1 2 3 ,,, 형식으로 출력
    
    for i in graph[v]: #v번과 인접한 노드들 중에
      if not visited[i]: #방문 안한 거 있으면
        queue.append(i) #queue에 추가해줌
        visited[i] = True #그리고 방문 표시
 
graph = [
  [],
  [2,3,8], #1번 노드와 인접한 노드들
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False]*9

bfs(graph, 1, visited)
