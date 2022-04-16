n = list(map(int, input()))
len_n = len(n)//2
l = sum(n[:len_n])
r = sum(n[len_n:])
if l == r:
  print("LUCKY")
else:
  print("READY")
