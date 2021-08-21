def solve (n):
  if n == 0:
    return 
  if n % 2 == 0 :
    print('(',end = '')
    solve(n-1)
  else :
    print(')', end='')
    solve(n-1)



n = int(input())

if n % 2 == 1 :
  print('')
else :
  solve(n)
  print('')
