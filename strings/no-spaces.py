s=input()
s = s.lower().split(" ")
print("_".join([word.title() for word in s]))