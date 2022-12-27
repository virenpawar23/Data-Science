from collections import Counter

s=input()
occurences_sorted_list = sorted(Counter(s).values())
upGrad_string = True

for i in range(1,max(occurences_sorted_list)+1):
    if i in occurences_sorted_list:
        occurences_sorted_list.remove(i)
    else:
        upGrad_string = False
        break

if upGrad_string:
    if len(occurences_sorted_list) == 0:
        print(upGrad_string)
    else:
        print(False)
else:
        print(False)