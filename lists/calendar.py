import ast

input_list1 = ast.literal_eval(input())
events = input_list1
wedding_date = int(input())
overlap = 0

for i in events:
    if i[0]<=wedding_date<=i[1]:
       overlap += 1 

print(overlap)