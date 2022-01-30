def bs(arr, target, start, end):
  if start>end:
    return None
  mid = (start+end)//2
  if arr[mid] == target:
    return mid
  elif arr[mid] > target:
    return bn(arr, target, start, mid-1)
  else:
    return bn(arr, target, mid+1, end)

n, target = list(map(int, input().split()))

arr = list(map(int, input().split()))

result = bn(arr, target, 0, n-1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result+1)
