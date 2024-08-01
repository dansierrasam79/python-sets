#find unique strings and occurrence
from collections import Counter as cnt
init_list = [0,1,2,3,4,5,6,7,8,9,10,5,4,3,2,1,0]

unique_nums = set(init_list)
print(unique_nums)

count_nums = cnt(init_list)
print(count_nums)
