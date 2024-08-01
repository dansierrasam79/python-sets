#find unique number combos
init_set = {0,1,2,3,4,5,6,7,8,9,10}
target_num = 12
final_list,final_list2 = [],[]
for num in init_set:
    for num2 in init_set:
        for num3 in init_set:
            total = num + num2 + num3
            if total == target_num:
                final_list.append([num,num2,num3])

for item in final_list:
    item.sort()

for lst in final_list:
    if lst not in final_list2:
        final_list2.append(lst)

print(final_list2)
