n = int(input())
a_list = list(map(int, input().split()))
sort_a_list = sorted(a_list)

booby = sort_a_list[-2]
print(a_list.index(booby)+1)