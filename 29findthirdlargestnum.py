#find third largest numbers
init_list = [0,1,2,3,4,5,6,7,8,9,10,9,7,5,3,1]
init_list2 = list(set(init_list))
init_list2.sort()
print(init_list2[-3])
