string1=input()
string2=input()
common_prefix = ""

for i,j in zip(string1,string2):
    if i.lower() == j.lower():
        common_prefix +=i
    else:
        break

if len(common_prefix):
    print(common_prefix)
else:
    print("-1")