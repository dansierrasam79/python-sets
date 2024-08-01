#find max product pair
init_set = {0,1,2,3,4,5,6,7,8,9,10}
max_prod, max_val,max_val2 = 0,0,0
for item in init_set:
    for item2 in init_set:
        prod = item*item2
        if max_prod < prod:
            max_prod = prod
            max_val = item
            max_val2 = item2
print(max_prod, max_val,max_val2)
