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

