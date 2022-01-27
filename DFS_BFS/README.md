
# DFS/BFS

| |DFS|BFS|
|:-|:-:|:-:|
|동작 원리|스택|큐|
|구현 방법|재귀 함수 이용|큐 자료구조 이용|


## 기본 
### Stack<br>
__정의__: 선입후출 혹은 후입선출 (First In Last Out)<br>

``` python
stack = []
stack.append(3)
stack.append(4)

print(stack) #=> [3,4]

stack.pop()

print(stack) #=> [3]
```


### Queue<br>
__정의__: 선입선출 (First In First Out)<br>

``` python
from collections import deque

queue = deque()

queue.append(3)
queue.append(4)

print(queue) #=> [3,4]

queue.popleft()

print(queue) #=> [4]
```

### 재귀 함수<br>

``` python
def recursive():
  print("recursive function")
  recursive()
 
recursive() #계속 반복해서 "recursive function"을 출력하다가 RecursionError 메세지를 출력하고 멈춤
```

#### *재귀 함수의 종료 조건*
__정의__: 종료 조건 명시하기<br>

``` python 
def recursive(i):
  if i == 100:
    return
  print(i, "번째 재귀 함수에서", i+1, "번째 재귀 함수를 호출합니다.")
  recursive(i+1)
  print(i, "번째 재귀 함수를 종료합니다.")
  
recursive(1)
```
재귀 함수는 내부적으로 스택 자료구조와 동일하기때문에 스택 자료구조를 활용하는 알고리즘은 재귀 함수로 간편하게 구현 가능!<br>
대표적인 것이 DFS<br>

``` python
#재귀 함수의 대표적인 팩토리얼 문제

#1. 반복적으로 구현한 팩토리얼
def factorial(n):
  result = 1
  for i in range(1, n+1):
    result *= i
  return result

#2. 재귀적으로 구현한 팩토리얼
def factorial2(n):
  if n<=1:
    return 1
  return n*factorial2(n-1)
```
-----


## [DFS](./DFS.py)
__정의__<br>
깊이 우선 탐색(Depth-First Search)<br>
특정한 경로를 탐색하다가 특정한 상황에서 최대한 깊숙이 들어가 노드 방문 후, 다시 도라가 다른 경로를 탐색하는 알고리즘<br>

__*POINT*__<br>
인접한 노드 중 방문하지 않은 노드가 여러 개 있다면 번호가 낮은 순서부터 처리<br>

-----

#### __예시 문제__<br>
#### [음료수 얼려 먹기](./ice.py)<br>

__설명__<br>
NxM 크기의 얼음 틀에서 0이 뚫린 부분, 1이 칸막이가 있는 부분이다. 0에 물을 부어 얼음을 얼릴 수 있는데 이는 상하좌우 연결되어 있으면 하나로 취급한다. 총 만들 수 있는 얼음 개수를 구하여라.<br>

__*POINT*__<br>
만약 현재 지점 기준 방문하지 않았다면 1로 방문 처리 후 재귀를 통해 주변에 방문하지 않은 곳을 방문해 True를 return한다. 만약 범위를 넘어가면 False를 return한다.<br>


## [BFS](./BFS.py)
__정의__<br>
너비 우선 탐색(Breadth First Search)<br>
가까운 노드부터 탐색하는 알고리즘<br>


__*POINT*__<br>
선입선출 방식인 Queue 자료구조를 이용하는 것이 정석<br>

__*알고리즘 이해!*__<br>
1. 제일 작은 노드 번호부터 시작해서 근접한 노드 번호를 다 큐에 집어 넣음<br>
2. 만약 인접 노드가 2,6,3이라면 큐에는 2,3,6 순서로 들어감<br>
3. 가장 먼저 들어온 2번 노드를 pop하여 그 주변 노드를 봄...이런 식으로 반복됨

-----

#### __예시 문제__<br>
#### [미로 탈출](./maze.py)<br>

__설명__<br>
NxM 크기의 미로에서 1은 괴물이 없는 곳 0은 괴물이 있는 곳이다. 괴물이 없는 길로 미로를 빠져나갈 수 있는 최소한의 칸 개수를 구하여라.<br>

__*POINT*__<br>
시작 지점에서 가까운 곳부터 탐색하는 BFS를 이용!<br>
* 덩어리로 뭉쳐서 풀어야하는 것은 DFS, 주변에 있는 걸 탐색하거나 길을 찾는 거면 BFS!
