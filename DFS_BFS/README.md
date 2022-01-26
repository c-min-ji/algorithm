
# DFS/BFS

#### *Stack & Queue*
<br>

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
