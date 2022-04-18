arr = []
n = input()
for i in n:
  arr.append(int(i))

for i in range(len(arr)-1):
  if arr[i]+arr[i+1] > arr[i]*arr[i+1]:
    arr[i+1] = arr[i]+arr[i+1]
  else:
    arr[i+1] = arr[i]*arr[i+1]
print(arr[-1])
