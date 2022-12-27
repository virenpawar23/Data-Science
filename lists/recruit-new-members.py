import ast
from statistics import mean
in1 = ast.literal_eval(input())
in2 = ast.literal_eval(input())

for i in in2:
    avg = mean(in1)
    in1.append(i)
    new_avg = mean(in1)
    # print(avg,new_avg)
    if not new_avg > avg  :
        in1.pop()
print(in1)