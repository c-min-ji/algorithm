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

#### 큌 정렬의 시간 복잡도: O(NlogN)
<hr>

## 계수 정렬

특정한 조건이 부합할 때만 
