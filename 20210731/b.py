password = input()

same_count = 0
stair_count = 0
for x in range(4):
  if x != 3  and password[x] == password[x+1]:
    same_count += 1
  elif x != 3 and int(password[x]) != 9 and int(password[x])+1 == int(password[x+1]):
    stair_count += 1
  elif x != 3 and int(password[x]) == 9 and int(password[x+1]) == 0:
    stair_count += 1

if same_count == 3 or stair_count == 3:
  print('Weak')
else :
  print('Strong')