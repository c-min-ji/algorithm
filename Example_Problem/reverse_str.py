num = input()
term_arr = [] #tuple 넣을 리스트
term = 1

for i in range(1, len(num)):
  if i == 1: #첫번째 원소일 경우
    if num[i] == num[i-1]:
      term += 1
    else:
      term_arr.append((term, num[i-1]))
      term = 1
  elif i+1 == len(num): #마지막 원소일 경우
    if num[i] == num[i-1]:
      term += 1
      term_arr.append((term, num[i]))
    else: #다르면 term 
      term_arr.append((term, num[i-1]))
      term = 1
      term_arr.append((term, num[i]))
  else:
    if num[i] == num[i-1]:
      term += 1
    else:
      term_arr.append((term, num[i-1]))
      term = 1

zero = 0
one = 0

for term, cnt in term_arr:
  if cnt=='0':
    zero +=1
  else:
    one+=1

print(min(zero, one))
