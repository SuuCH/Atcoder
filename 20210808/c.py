def del_heigt(card_list):
  for i in range(h):
    del card_list[i][0]


h,w,n = map(int,input().split())
card_list = [[-1]*w for i in range(h)]
for i in range(n):
  ai, bi = map(int, input().split())
  card_list[ai-1][bi-1] = i+1

for i in range(h):
  for j in range(w):
    if card_list[i][j] != -1:
      break
    if j == w-1:
      card_list[i].clear()

for i in range(w):
  for j in range(h):
    if len(card_list[j]) == 0:
      continue
    if card_list[j][i] != -1:
      break
    if j == h-1:
      del_heigt(card_list)

print(card_list)