# 정렬(Sorting)
__*데이터를 특정한 기준에 따라서 순서대로 나열*__<br>
<br>

## 정렬 알고리즘 종류
> * 선택 정렬<br> 
> * 삽입 정렬<br> 
> * 퀵 정렬<br> 
> * 계수 정렬<br>

## 선택 정렬
가장 작은 데이터를 선택해 가장 앞에 있는 데이터와 교환하는 과정을 반복<br>

``` python
array = [5,6,7,3,4,1]

for i in range(len(array)): #array[i]와 array[min_index] 계속 비교하면서 작은 거 찾아내기
  min_index = i
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i] #서로 바꿔주기
  
print(array) #=> [1,3,4,5,6,7]
```

+) 스와프 코드
```python 
array = [3,5]
array[0], array[1] = array[1],array[0]

#=> array = [5,3]
```

#### 선택 정렬의 시간 복잡도: O(N^3)
선택 정렬은 알고리즘에 사용하기에는 느린 편<br>
<hr>

## 선택 정렬
특정한 데이터를 적절한 위치에 '삽입'한다는 의미<br>

### 알고리즘
선택 정렬은 맨 처음 데이터는 정렬되었다는 가정 하에 시작하기에 2번째 데이터부터 확인한다. 
<br>

```python
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
  for j in range(i, 0, -1): #맨 앞부터 훑음
    if array[j]<array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]
    else:
      break
print(array) #=> [1,3,4,5,6,7,8,9,0]
```

## 퀵 정렬
가장 빠른 알고리즘<br>
퀵 정렬에서는 피벗이라는 중심 기준이 필요<br>
대표적인 분할 방식에는 호어 분할이 있음
* 기본적인 형태의 퀵 정렬

```python
array = [3,5,1,8,4,9,2]

def quick_sort(array, start, end):
  if start>=end:
    return
  pivot = start
  left = start+1
  right = end
  while left<=right:
    while left<=end and array[left]<=array[pivot]:
      left+=1
    while right>start and array[right]>=array[pivot]:
      right-=1
    if left>right:
      array[right], array[pivot] = array[pivot], array[right]
    else:
      array[left], array[right] = array[right], array[left]
  quick_sort(array, start, right-1)
  quick_sort(array, right+1, end)
  
quick_sort(array,0,len(array)-1)
print(array) #=> [1,2,3,4,5,8,9]
```
<br>

* 파이썬의 장점을 살린 퀵 정렬

```python
arrry = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
  if len(array)<=1:
    return array
  pivot = array[0]
  tail = array[1:]
  
  left_side = [x for x in tail if x<=pivot]
  right_side = [x for x in tail if x>pivot]
  
  return quick_sort(left_side) + [pivot] + qucik_sort(right_side)
  
print(quick_sort(array)) #=> [0,1,2,3,4,5,6,7,8,9]
```

#### 퀵 정렬의 시간 복잡도: O(NlogN)
<hr>

## 계수 정렬

특정한 조건이 부합할 때만 사용할 수 있으나 굉장히 빠른 알고리즘임.<br>
0-9까지의 숫자가 담긴 리스트에 각 번호가 몇 번 나왔는 지 카운팅하여 리스트를 다시 출력한다.<br>

```python 
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

cnt = [0]* (max(array)+1)

for i in range(len(array)): #array에 있는 숫자를 cnt[숫자]+1 해줌
  cnt[array[i]] += 1
 
for i in range(len(array)):
  for j in range(cnt[i]): #cnt개수만큰 i를 프린트
    print(i, end=" ") #=> 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9
```

#### 계수 정렬의 시간 복잡도: O(N+K)
cf. 기수 정렬과 더불어 제일 빠르다. 기수 정렬을 계수 정렬보다는 느리지만 처리할 수 있는 수가 크다.
<br>

#### 계수 정렬의 공간 복잡도: O(N+K)

<hr>

## 파이썬 정렬 라이브러리

#### sorted()
퀵 정렬과 동작 방식이 비슷한 병합 정렬을 기반으로 만들어짐.<br>
병합 정렬은 퀵 정렬보다 느리긴 하지만 최악의 경우에도 시간 복잡도 O(NlogN)을 보장함.<br>
리스트, 딕셔너리 형식을 입력 받아 정렬된 결과 출력.

```python
arr = [7,8,2,4,5,9]

result = sorted(arr)
print(result) #=> [2,4,5,7,8,9]
```

#### sort()
내부 원소를 바로 정렬하는 것. 그래서 원래 주어진 배열이 변하는 것<br>

```python
arr = [7,5,9,0,3,1,6,2,4,8]

arr.sort()
print(arr) #=> [0,1,2,3,4,5,6,7,8,9]
```

#### key 활용
sorted() 혹은 sort()를 사용할 때 key 매개 변수를 사용할 수 있다.

```python
arr = [('banana',2),('apple',5),('carrot',3)]

def setting(data):
  return data[1]
 
result = sorted(array, key=setting)
print(result) #=> [('banana',2),('carrot',3),('apple',5)]
```

#### 정렬 라이브러리의 시간 복잡도: O(NlogN)
<hr>

### 연습 문제
[1. 위에서 아래로](./upanddown.py)

> __문제 설명__<br>
> 수열을 내림차순으로 정렬하라

>__point__<br>
>sorted() 사용

<br>

[2. 성적이 낮은 순서로 학생 출력하기](./student.py)

> __문제 설명__<br>
> 성적이 낮은 순서대로 학생들의 이름을 출력하라

>__point__<br>
>sorted() 사용
<br>

[3. 두 배열의 원소 교체](./change.py)

> __문제 설명__<br>
> A와 B 리스트 사이에서 서로 원소를 K번 바꿀 수 있는데 A리스트의 합이 최대가 되게하라.

>__point__<br>
>A에서 가장 작은 원소를 골라서 B에서 가장 큰 원소와 교체
