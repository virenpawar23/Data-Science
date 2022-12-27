import ast
from statistics import mean

input_str = input()
input_list = ast.literal_eval(input_str)
check= input_list[1]
if check > mean(input_list[0]):
    print(True)
else:
    print(False)