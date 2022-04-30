n = list(input())
n = sorted(n)
st = ''
num = 0
for i in n:
  if i.isalpha() == True:
    st += i
  else:
    num += int(i)
st += str(num)
print(st)
