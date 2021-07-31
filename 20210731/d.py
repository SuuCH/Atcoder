import heapq

q = int(input())

heap_list = []
min_list = []
s_sum = 0
for i in range(q):
  string = input()
  tmplist = string.split()
  if int(tmplist[0]) == 1:
    heapq.heappush(heap_list, int(tmplist[1])-s_sum)
  elif int(tmplist[0]) == 2:
    s_sum += int(tmplist[1])
  elif int(tmplist[0]) == 3:
    tmp_min = heapq.heappop(heap_list)
    min_list.append(tmp_min+s_sum)

print(*min_list)



