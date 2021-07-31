n = int(input())
s = input()
str_list = list(s)

for i in range(n):
  if str_list[i] == '1' and i % 2 == 0:
    print('Takahashi')
    break
  elif str_list[i] == '1' and i % 2 == 1:
    print('Aoki')
    break
