import sys

a, b = map(int,input().split())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))


sort_a_list = sorted(a_list)
sort_b_list = sorted(b_list)

i = 0
j = 0
list_min = abs(sort_a_list[i] - sort_b_list[j])
while i < a and j < b:
  if abs(sort_a_list[i] - sort_b_list[j]) < list_min:
    list_min = abs(sort_a_list[i] - sort_b_list[j])
  
  if sort_a_list[i] < sort_b_list[j]:
    i+=1
  else:
    j+=1

print(list_min)
  

