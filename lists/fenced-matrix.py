import ast
m,n = ast.literal_eval(input())

for i in range(m):
    row = []
    for j in range(n):
        if i == 0 or i == (m-1) or j == 0 or j == (n-1):
           row.append(1)
        else:
            row.append(0)
    print((row))
    