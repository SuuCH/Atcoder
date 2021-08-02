import math
def solve(n, k, l,a_list, mid):
  cnt = 0
  pre = 0
  for i in range(n):
    if a_list[i] - pre >= mid and l - a_list[i] >= mid:
      cnt += 1
      pre = a_list[i]
  if cnt >= k:
    return True
  return False


n,l = map(int,input().split())
k = int(input())
a_list = list(map(int, input().split()))


left = -1
right = l + 1

while right - left > 1 :
  mid = left + (right - left) /2
  if solve(n,k,l,a_list,mid) == False :
    right = mid
  else :
    left = mid

print(math.ceil(left))