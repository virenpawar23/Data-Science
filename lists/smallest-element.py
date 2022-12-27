import ast

input_str = input()
input_list = ast.literal_eval(input_str)

print(min(input_list))