s = input()
prefix = ""
for i in s:
    if i.lower() in 'aeiou':
        s = s.replace(i,'')
        prefix += i  
print(prefix+s)