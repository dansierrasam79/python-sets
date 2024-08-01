#remove intersection
init_set = {0,1,2,3,4,5,6,7,8,9,10}
init_set2 = {2,5,6}
init_set3 = init_set.intersection(init_set2)
for item in init_set3:
    init_set.remove(item)
print(init_set)
