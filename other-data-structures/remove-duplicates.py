import ast
from collections import Counter

in1 = ast.literal_eval(input())
print([*Counter(in1)])