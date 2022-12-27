from collections import Counter

s1 = input()
s2 = input()

l1 = [*s1]+[*s2]
anagrams = True

for i in set(Counter(l1).values()):
    if i != 2:
        anagrams = False
print(anagrams)