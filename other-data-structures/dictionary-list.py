import ast

input_str = input()
input_dict = ast.literal_eval(input_str)
op_list = []

for i,j in input_dict.items():
    for val in j:
        op_list.append(i+"_"+val)
print(op_list)