def sequential(n, target, array):
  for i in range(n):
    if array[i]==target:
      return i+1
      
print("생성할 원소 개수를 입력한 다음 한 칸을 띄고 찾을 문자열을 입력하시오.")

input_data = input().split()
n = int(input_data[0])
tartget = input_data[1]

print("앞서 적은 원소 개수만크 문자열을 입력하시오. 구분은 띄어쓰기로 합니다.")
array = input().split()

print(sequential(n, target, array)
