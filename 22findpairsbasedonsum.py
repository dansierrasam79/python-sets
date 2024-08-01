init_list = [0,1,2,3,4,5,6,7,8,9,10,5,4,3,2,1]
init_set = list(set(init_list))
final_list,final_list2 = [],[]
sum_value = 5
for i in range(0,len(init_set)):
    total = 0
    for j in range(0,len(init_set)):
        total = init_set[i] + init_set[j]
        if total == sum_value:
            final_list.append([init_set[i],init_set[j]])

for item in final_list:
    item.sort()

for item in final_list:
    if item not in final_list2:
        final_list2.append(item)
print(final_list2)
