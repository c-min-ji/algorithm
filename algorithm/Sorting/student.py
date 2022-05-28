n = int(input())

arr = []
for i in range(n):
  input_data = input().split()
  arr.append((input_data[0],int(input_data[1])))

arr = sorted(arr, key=lambda student: student[1]) #점수 기준으로 정렬

for student in array:
  print(student[0], end=' ')
