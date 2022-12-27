in_list = input().split(",")
m = int(in_list[0])
c = int(in_list[1])

chocolates = m//c
wrappers = chocolates

while wrappers//3!=0:
    chocolates += wrappers//3
    wrappers = wrappers//3 + wrappers%3

print(chocolates)