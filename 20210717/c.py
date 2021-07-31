n,k = map(int,input().split())
c_list = list(map(int, input().strip().split()))

tmp_list_unique = list(set(c_list[:k]))
count_max = len(tmp_list_unique)

for i in range(n):
  if i+k-1 >= n-1:
    break
  
  tmp_list = tmp_list_unique[1:k]
  tmp_list.append(c_list[k+1])

  if count_max < count:
    count_max = count
  if count_max >= k:
    break

print(count_max)
    
