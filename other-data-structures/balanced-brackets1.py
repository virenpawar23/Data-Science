from collections import Counter
inp="){[[]]}())()"
dict1 = dict(Counter(inp))
if len(dict1.keys()) and len(dict1.keys())%2==0:
    if (dict1['('] == dict1[')']) and (dict1['{'] == dict1['}']) and (dict1['['] == dict1[']']):
        print("Yes")
    else:
        print("No")
else:
    print("No")