from functools import reduce
number= int(input())

if number == 0:
    print(1)
elif number < 0:
    print(-1)
else:
    print(reduce(lambda a,b:a*b,range(1,number+1)))