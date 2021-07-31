n,a,x,y = map(int,input().split())

sum = 0
for i in range(n):
  if i < a :
    sum += x
  else:
    sum += y

print(sum)
